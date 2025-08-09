from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import os
from config import EMBEDDINGS_DIR, EMBEDDING_MODEL

def embed_chunks(video_id, chunks):
    os.makedirs(EMBEDDINGS_DIR, exist_ok=True)
    model = SentenceTransformer(EMBEDDING_MODEL)
    embeddings = model.encode(chunks)

    # Save FAISS index
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings))

    faiss.write_index(index, os.path.join(EMBEDDINGS_DIR, f"{video_id}.index"))

    # Save chunks text
    with open(os.path.join(EMBEDDINGS_DIR, f"{video_id}_chunks.txt"), "w", encoding="utf-8") as f:
        for chunk in chunks:
            f.write(chunk + "\n")

    return index
