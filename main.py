from src.pipeline import run_rag_pipeline

if __name__ == "__main__":
    query = input("Введите ваш запрос: ")
    run_rag_pipeline(query)

