# Этот модуль строит FAISS-индекс из всех векторов, делая некую базу, по которой потом можно быстро искать по смыслу

import faiss
import json

from src.config import INDEX_PATH, CHUNKS_PATH
from src.embedder import embed_texts

def build_index():
    with open(CHUNKS_PATH, "r", encoding="utf-8") as f:
        chunks = json.load(f)

    embeddings = embed_texts(chunks)
    dim = embeddings.shape[1]

    index = faiss.IndexFlatIP(dim)
    index.add(embeddings)

    faiss.write_index(index, INDEX_PATH)
    return index, chunks

