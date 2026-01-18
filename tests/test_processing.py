from data_ingestion.pdf_loader import load_pdf
from processing.text_cleaner import clean_text
from processing.chunker import chunk_text

pages = load_pdf("data/pdfs/wolfram_didmoid_syndrome.pdf")

sample_page = pages[0]["text"]
cleaned = clean_text(sample_page)
chunks = chunk_text(cleaned)

print(f"Original length: {len(sample_page)}")
print(f"Cleaned length: {len(cleaned)}")
print(f"Total chunks created: {len(chunks)}")

print("\n--- FIRST CHUNK PREVIEW ---\n")
print(chunks[0][:800])
