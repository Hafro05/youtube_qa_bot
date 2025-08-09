from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
import os
from config import TRANSCRIPTS_DIR

def fetch_transcript(video_id, preferred_lang="en"):
    os.makedirs(TRANSCRIPTS_DIR, exist_ok=True)
    transcript_path = os.path.join(TRANSCRIPTS_DIR, f"{video_id}.txt")
    
    # ✅ Skip if transcript already exists
    if os.path.exists(transcript_path):
        print(f"✅ Using cached transcript: {transcript_path}")
        with open(transcript_path, "r", encoding="utf-8") as f:
            return f.read()

    try:
        # Get list of all available transcripts for the video
        transcript_list = YouTubeTranscriptApi().list(video_id)

        # Try to get preferred language (e.g., English)
        try:
            transcript = transcript_list.find_transcript([preferred_lang])
        except:
            # If preferred language not found, get first available transcript
            transcript = next(iter(transcript_list))

        # Fetch the actual transcript text
        transcript_data = transcript.fetch()
        text = " ".join([t.text for t in transcript_data])

        # Save locally
        path = os.path.join(TRANSCRIPTS_DIR, f"{video_id}.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)

        print(f"Transcript language used: {transcript.language}")
        return text

    except TranscriptsDisabled:
        print("❌ Transcripts are disabled for this video.")
        return None
    except Exception as e:
        print(f"❌ Could not fetch transcript: {e}")
        return None
