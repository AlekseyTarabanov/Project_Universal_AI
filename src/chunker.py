# Берёт большой текст и режет его на маленькие куски, чтобы потом поиск работал нормально. Результат сохраняет, чтобы остальные модули могли это использовать

import json
import nltk
nltk.download("punkt")
from nltk.tokenize import sent_tokenize

from src.config import CHUNKS_PATH

def split_into_chunks(text, max_chunk_size, overlap_ratio=0.25):
    sentences = sent_tokenize(text, language="russian")

    chunks = []
    current_chunk = []
    current_len = 0

    overlap_len = int(max_chunk_size * overlap_ratio)

    for sent in sentences:
        sent_len = len(sent)

        # если предложение помещается в текущий чанк
        if current_len + sent_len <= max_chunk_size:
            current_chunk.append(sent)
            current_len += sent_len
        else:
            # сохраняем чанк
            chunk_text = " ".join(current_chunk).strip()
            chunks.append(chunk_text)

            # формируем overlap — последние предложения
            overlap_chunk = []
            overlap_current_len = 0

            for prev_sent in reversed(current_chunk):
                overlap_current_len += len(prev_sent)
                overlap_chunk.insert(0, prev_sent)
                if overlap_current_len >= overlap_len:
                    break

            # начинаем новый чанк с overlap
            current_chunk = overlap_chunk + [sent]
            current_len = overlap_current_len + sent_len

    if current_chunk:
        chunks.append(" ".join(current_chunk).strip())

    # сохраняем чанки
    with open(CHUNKS_PATH, "w", encoding="utf-8") as f:
        json.dump(chunks, f, ensure_ascii=False, indent=2)

    return chunks


