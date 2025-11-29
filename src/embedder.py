# Тут мы гоняем текст через модель эмбеддингов и получаем вектора, превращаем текст в числа, чтобы FAISS потом мог сравнивать похожие куски

import torch
from sentence_transformers import SentenceTransformer
from sklearn.preprocessing import normalize

from src.config import EMBEDDING_MODEL

device = "cuda" if torch.cuda.is_available() else "cpu"
model = SentenceTransformer(EMBEDDING_MODEL).to(device)

def embed_texts(texts):
    emb = model.encode(texts, convert_to_numpy=True, show_progress_bar=False)
    return normalize(emb)

