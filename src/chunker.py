# Берёт большой текст и режет его на маленькие куски, чтобы потом поиск работал нормально. Результат сохраняет, чтобы остальные модули могли это использовать

import json
import nltk
nltk.download("punkt")
from nltk.tokenize import sent_tokenize

from src.config import CHUNK_SIZE, CHUNKS_PATH

def split_into_chunks(text, max_chunk_size=CHUNK_SIZE):
    sentences = sent_tokenize(text, language="russian")
    chunks = []
    current_chunk = ""

    for sent in sentences:
        # добавляем предложение в текущий чанк
        if len(current_chunk) + len(sent) <= max_chunk_size:
            if current_chunk:
                current_chunk += " " + sent
            else:
                current_chunk = sent
        else:
            chunks.append(current_chunk.strip())
            current_chunk = sent

    if current_chunk:
        chunks.append(current_chunk.strip())

    # сохраняем чанки
    with open(CHUNKS_PATH, "w", encoding="utf-8") as f:
        json.dump(chunks, f, ensure_ascii=False, indent=2)

    return chunks
