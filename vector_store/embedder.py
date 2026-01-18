# vector_store/embedder.py
from sentence_transformers import SentenceTransformer
import numpy as np

class Embedder:
    """
    Generates sentence embeddings using Sentence-Transformers.
    """

    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

    def embed_texts(self, texts: list[str]) -> np.ndarray:
        """
        Convert list of texts into embeddings.
        """
        embeddings = self.model.encode(
            texts,
            show_progress_bar=True,
            convert_to_numpy=True,
            normalize_embeddings=True
        )
        return embeddings
