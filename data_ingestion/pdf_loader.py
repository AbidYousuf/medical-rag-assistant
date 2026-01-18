# data_ingestion/pdf_loader.py
import fitz  # PyMuPDF
from pathlib import Path

def load_pdf(pdf_path: str):
    """
    Extract text from a PDF page by page.
    Returns list of dicts with document name, page number and text.
    """
    pdf_path = Path(pdf_path)
    document = fitz.open(pdf_path)

    pages = []

    for page_index in range(len(document)):
        page = document.load_page(page_index)
        text = page.get_text("text").strip()

        if text:
            pages.append({
                "document": pdf_path.name,
                "page": page_index + 1,
                "text": text
            })

    return pages
