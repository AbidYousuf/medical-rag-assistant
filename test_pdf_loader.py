from pathlib import Path
from data_ingestion.pdf_loader import load_pdf

pdf_dir = Path("data/pdfs")

all_pages = []

for pdf_file in pdf_dir.glob("*.pdf"):
    pages = load_pdf(pdf_file)
    print(f"{pdf_file.name} → {len(pages)} pages extracted")
    all_pages.extend(pages)

print(f"\nTOTAL pages extracted: {len(all_pages)}")

print("\n--- SAMPLE TEXT (FIRST PAGE) ---\n")
print(all_pages[0]["text"][:1000])
