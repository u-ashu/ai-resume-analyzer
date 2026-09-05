import re


def clean_text(text: str) -> str:
    text = text.lower()

    # Replace newlines with spaces
    text = re.sub(r"\n", " ", text)

    # Replace punctuation with spaces
    text = re.sub(r"[^a-zA-Z0-9\s]", " ", text)

    # Remove extra whitespace
    text = re.sub(r"\s+", " ", text)

    return text.strip()