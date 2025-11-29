# Берёт большой текст и режет его на маленькие куски, чтобы потом поиск работал нормально. Результат сохраняет, чтобы остальные модули могли это использовать

import json
from src.config import CHUNK_SIZE, CHUNKS_PATH

def split_into_chunks(text, size=CHUNK_SIZE):
    chunks = []
    for i in range(0, len(text), size):
        chunk = text[i:i + size].strip()
        if len(chunk) > 20:
            chunks.append(chunk)

    with open(CHUNKS_PATH, "w", encoding="utf-8") as f:
        json.dump(chunks, f, ensure_ascii=False, indent=2)

    return chunks

