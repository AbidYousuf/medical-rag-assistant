from retriever.semantic_retriever import SemanticRetriever

retriever = SemanticRetriever(embedding_dim=384)

query = "What are the clinical features of Wolfram syndrome?"

results = retriever.retrieve(query, top_k=3)

for idx, res in enumerate(results, 1):
    print(f"\nResult {idx}")
    print(f"Score: {res['score']}")
    print(f"Document: {res['metadata']['document']}")
    print(f"Page: {res['metadata']['page']}")
    print(res['metadata'])
