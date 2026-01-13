# Идея: Пересчитать cosine similarity только для TOP_K и отсортировать заново
# учитывает ключевые слова, учитывает длину ответа, учитывает точное соответствие вопросу

import numpy as np
from src.embedder import embed_texts

def rerank(query, chunks):
    q_emb = embed_texts([query])[0]
    c_embs = embed_texts(chunks)

    scored = []
    for chunk, emb in zip(chunks, c_embs):
        score = float(emb @ q_emb)
        scored.append((chunk, score))

    scored.sort(key=lambda x: x[1], reverse=True)
    return scored

