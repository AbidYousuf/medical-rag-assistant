# processing/text_cleaner.py
import re

def clean_text(text: str) -> str:
    """
    Normalize and clean raw PDF text.
    """
    # Remove references section if present
    text = re.split(r'\nreferences\b', text, flags=re.IGNORECASE)[0]

    # Remove excessive newlines
    text = re.sub(r'\n+', ' ', text)

    # Normalize whitespace
    text = re.sub(r'\s+', ' ', text)

    # Remove non-ASCII characters
    text = re.sub(r'[^\x20-\x7E]', '', text)

    return text.strip()
