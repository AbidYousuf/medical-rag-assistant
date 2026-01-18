from rag.rag_pipeline import RAGPipeline

rag = RAGPipeline()

query = "What are the clinical features of Wolfram syndrome?"

answer, sources = rag.run(query, top_k=3)

print("\nANSWER:\n")
print(answer)

print("\nSOURCES:")
for s in sources:
    print(s["metadata"])
