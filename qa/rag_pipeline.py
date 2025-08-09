import subprocess
from config import LLM_MODEL
from retriever.vector_search import search_chunks

def ask_question(video_id, question):
    context_chunks = search_chunks(video_id, question, top_k=3)
    context = "\n".join(context_chunks)

    prompt = f"Answer the question using only this transcript:\n{context}\n\nQuestion: {question}"

    # Run local LLM with Ollama
    result = subprocess.run(
        ["ollama", "run", LLM_MODEL, prompt],
        capture_output=True, text=True
    )

    return result.stdout.encode("utf-8", errors="ignore").strip()
