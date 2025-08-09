import re
from ingestion.transcript_fetcher import fetch_transcript
from ingestion.chunker import chunk_text
from ingestion.embedder import embed_chunks
from qa.rag_pipeline import ask_question

def extract_video_id(url):
    match = re.search(r"v=([a-zA-Z0-9_-]{11})", url)
    return match.group(1) if match else None

if __name__ == "__main__":
    youtube_url = input("Enter YouTube video URL: ")
    video_id = extract_video_id(youtube_url)
    if not video_id:
        print("Invalid YouTube URL.")
        exit()

    print("\nFetching transcript...")
    text = fetch_transcript(video_id)

    print("Chunking transcript...")
    chunks = chunk_text(text)

    print("Embedding chunks...")
    embed_chunks(video_id, chunks)

    print("\n✅ Ready! You can now ask questions about the video.")
    while True:
        q = input("\nYour question (or 'quit'): ")
        if q.lower() == "quit":
            break
        answer = ask_question(video_id, q)
        print(f"\nAnswer: {answer}")
