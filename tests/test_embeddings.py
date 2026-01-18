from data_ingestion.pdf_loader import load_pdf
from processing.text_cleaner import clean_text
from processing.chunker import chunk_text
from vector_store.embedder import Embedder
from vector_store.faiss_store import FAISSVectorStore

# Load PDF
pages = load_pdf("data/pdfs/wolfram_didmoid_syndrome.pdf")

texts = []
metadata = []

for page in pages:
    cleaned = clean_text(page["text"])
    chunks = chunk_text(cleaned)

    for chunk in chunks:
        texts.append(chunk)
        metadata.append({
            "document": page["document"],
            "page": page["page"],
            "text": chunk
        })

print(f"Total chunks: {len(texts)}")

# Embed
embedder = Embedder()
embeddings = embedder.embed_texts(texts)

print(f"Embedding shape: {embeddings.shape}")

# Store in FAISS
store = FAISSVectorStore(embedding_dim=embeddings.shape[1])
store.add(embeddings, metadata)
store.save()

print("FAISS index created and saved successfully.")
