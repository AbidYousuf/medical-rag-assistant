from rag.rag_pipeline import RAGPipeline

rag = RAGPipeline()

query = "What are the clinical features of Wolfram syndrome?"

prompt = rag.build_prompt(query, top_k=3)

print(prompt)
