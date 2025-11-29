# Превращает запрос в вектор и ищет по FAISS, какие куски текста лучше всего подходят. Возвращает найденные фрагменты

import json
import faiss

from src.config import INDEX_PATH, CHUNKS_PATH, TOP_K
from src.embedder import embed_texts

def search(query):
    index = faiss.read_index(INDEX_PATH)

    with open(CHUNKS_PATH, "r", encoding="utf-8") as f:
        chunks = json.load(f)

    q_emb = embed_texts([query])
    _, ids = index.search(q_emb, TOP_K)

    return [chunks[i] for i in ids[0]]

