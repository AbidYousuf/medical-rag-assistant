# vector_store/faiss_store.py
import faiss
import numpy as np
import pickle
from pathlib import Path

class FAISSVectorStore:
    """
    FAISS-based vector store for similarity search.
    """

    def __init__(self, embedding_dim: int, index_path="vector_store/index.faiss", meta_path="vector_store/meta.pkl"):
        self.embedding_dim = embedding_dim
        self.index_path = Path(index_path)
        self.meta_path = Path(meta_path)

        self.index = faiss.IndexFlatIP(embedding_dim)
        self.metadata = []

    def add(self, embeddings: np.ndarray, metadatas: list[dict]):
        self.index.add(embeddings.astype("float32"))
        self.metadata.extend(metadatas)

    def save(self):
        faiss.write_index(self.index, str(self.index_path))
        with open(self.meta_path, "wb") as f:
            pickle.dump(self.metadata, f)

    def load(self):
        self.index = faiss.read_index(str(self.index_path))
        with open(self.meta_path, "rb") as f:
            self.metadata = pickle.load(f)

    # def search(self, query_embedding: np.ndarray, top_k: int = 5):
    #     scores, indices = self.index.search(query_embedding.astype("float32"), top_k)
    #     results = []

    #     for idx, score in zip(indices[0], scores[0]):
    #         results.append({
    #             "score": float(score),
    #             "metadata": self.metadata[idx]
    #         })

    #     return results
    def search(self, query_embedding: np.ndarray, top_k: int = 5):
        scores, indices = self.index.search(query_embedding.astype("float32"), top_k)
        results = []

        for idx, score in zip(indices[0], scores[0]):
            item = self.metadata[idx]
            results.append({
            "score": float(score),
            "metadata": item,
            "text": item.get("text", "")
        })

        return results
