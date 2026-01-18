# rag/rag_pipeline.py
from retriever.semantic_retriever import SemanticRetriever
from llm.ollama_client import OllamaClient

class RAGPipeline:
    def __init__(self, embedding_dim=384):
        self.retriever = SemanticRetriever(embedding_dim)
        self.llm = OllamaClient()

    def run(self, query: str, top_k: int = 3):
        results = self.retriever.retrieve(query, top_k)

        context = ""
        for res in results:
            context += (
                f"Source: {res['metadata']['document']} "
                f"(Page {res['metadata']['page']})\n"
                f"{res.get('text', '')}\n\n"
            )

        prompt = f"""
You are a medical assistant.
Answer the question using ONLY the information in the context below.
If the answer is not present, say "Information not found in documents."

Context:
{context}

Question:
{query}

Answer:
"""

        answer = self.llm.generate(prompt)
        return answer, results
