# Превращает запрос в вектор и ищет по FAISS, какие куски текста лучше всего подходят. Возвращает найденные фрагменты

import json
import faiss

from src.config import INDEX_PATH, CHUNKS_PATH
from src.embedder import embed_texts

def search(query, top_k):
    index = faiss.read_index(INDEX_PATH)

    with open(CHUNKS_PATH, "r", encoding="utf-8") as f:
        chunks = json.load(f)

    q_emb = embed_texts([query])
    _, ids = index.search(q_emb, top_k)

    # фильтруем дубликаты
    seen = set()
    results = []
    for i in ids[0]:
        chunk = chunks[i]
        if chunk not in seen:
            results.append(chunk)
            seen.add(chunk)

    return results

