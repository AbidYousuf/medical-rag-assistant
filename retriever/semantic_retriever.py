# retriever/semantic_retriever.py
import numpy as np
from vector_store.embedder import Embedder
from vector_store.faiss_store import FAISSVectorStore

class SemanticRetriever:
    """
    Retrieves top-k relevant chunks using FAISS.
    """

    def __init__(self, embedding_dim: int):
        self.embedder = Embedder()
        self.store = FAISSVectorStore(embedding_dim)
        self.store.load()

    def retrieve(self, query: str, top_k: int = 5):
        query_embedding = self.embedder.embed_texts([query])
        results = self.store.search(query_embedding, top_k)
        return results
