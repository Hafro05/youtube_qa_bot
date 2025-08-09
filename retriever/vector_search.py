import faiss
import numpy as np
import os
from sentence_transformers import SentenceTransformer
from config import EMBEDDINGS_DIR, EMBEDDING_MODEL

def search_chunks(video_id, query, top_k=3):
    # Load index
    index_path = os.path.join(EMBEDDINGS_DIR, f"{video_id}.index")
    chunks_path = os.path.join(EMBEDDINGS_DIR, f"{video_id}_chunks.txt")

    index = faiss.read_index(index_path)
    with open(chunks_path, "r", encoding="utf-8") as f:
        chunks = [line.strip() for line in f.readlines()]

    model = SentenceTransformer(EMBEDDING_MODEL)
    query_emb = model.encode([query])
    distances, indices = index.search(np.array(query_emb), top_k)

    results = [chunks[i] for i in indices[0]]
    return results
