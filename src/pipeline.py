# просто оркестратор — запускает всё по порядку

from src.dataset_loader import load_text
from src.chunker import split_into_chunks
from src.index_builder import build_index
from src.searcher import search
from src.config import DATASET_PATH, RESULT_PATH

def run_rag_pipeline(query):
    print("[1] Чтение датасета...")
    text = load_text(DATASET_PATH)

    print("[2] Разбиение на чанки...")
    chunks = split_into_chunks(text)

    print("[3] Создание FAISS индекса...")
    build_index()

    print("[4] Поиск по запросу...")
    results = search(query)

    print("[5] Запись результата в result.txt...")
    with open(RESULT_PATH, "w", encoding="utf-8") as f:
        for r in results:
            f.write(r + "\n\n")

    print("[+] Готово!")

