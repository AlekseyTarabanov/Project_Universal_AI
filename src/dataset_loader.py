# Отвечает за чтение исходного .txt файла. Обеспечивает единый способ загрузки данных в систему
def load_text(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

