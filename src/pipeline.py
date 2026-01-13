# просто оркестратор — запускает всё по порядку

from src.dataset_loader import load_text
from src.chunker import split_into_chunks
from src.index_builder import build_index
from src.searcher import search
from src.config import DATASET_PATH, RESULT_PATH
from src.param_optimizer import optimize_params
from src.reranker import rerank
from src.postprocess import deduplicate_by_prefix
from src.keyword_boost import keyword_boost

def run_rag_pipeline(query):
    print("[1] Чтение датасета...")
    text = load_text(DATASET_PATH)
    chunk_size, top_k = optimize_params(text, query)

    print("[2] Разбиение на чанки...")
    chunks = split_into_chunks(text, chunk_size)

    print("[3] Создание FAISS индекса...")
    build_index()

    print("[4] Поиск по запросу...")
    retrieved_chunks = search(query, top_k)

    # rerank возвращает (chunk, score)
    ranked = rerank(query, retrieved_chunks)
    ranked = keyword_boost(query, ranked)
    ranked = sorted(ranked, key=lambda x: x[1], reverse=True)

    print("\n[DEBUG] Rerank результаты:")
    for chunk, score in ranked:
        print(f"{score:.3f} | {chunk[:80]}...")


    SCORE_THRESHOLD = 0.72
    print(f"[5] Фильтрация по уверенности. {SCORE_THRESHOLD} ")

    filtered = [
        chunk for chunk, score in ranked
        if score >= SCORE_THRESHOLD
    ]

    # если слишком жёстко отфильтровали — оставляем хотя бы лучший
    if len(filtered) < 1:
        filtered = [ranked[0][0]]

    elif len(filtered) < 2:
            filtered.append(ranked[1][0])



    print("[6] Убираем дубли Overlap")
    filtered_dub = deduplicate_by_prefix(filtered)

    MAX_CONTEXT_CHUNKS = 2
    print(f"[7] Ограничиваем кол-во контекста до {MAX_CONTEXT_CHUNKS} чанков")
    filtered_cut = filtered_dub[:MAX_CONTEXT_CHUNKS]

    print("[8] Запись результата в result.txt...")
    with open(RESULT_PATH, "w", encoding="utf-8") as f:
        for chunk in filtered_cut:
            f.write(chunk.strip() + "\n\n")

    print("[+] Готово!")

    print(f"\n\nВывод резултата до фильтрации:\n{retrieved_chunks}")
    print(f"\n\nВывод резултата до вырезания дублей:\n{filtered}")
    print(f"\n\nВывод резултата до ограничивания контекста :\n{filtered_dub}")
    print(f"\n\nВывод резултата:\n{filtered_cut}")

