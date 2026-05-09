from pathlib import Path
from pypdf import PdfReader


def extract_text(file_path: str) -> str:
    path = Path(file_path)

    if path.suffix.lower() == ".txt":
        return path.read_text(encoding="utf-8")

    return "Text extraction is not supported for this file type yet."


def extract_pdf_text(path: Path) -> str:
    reader = PdfReader(str(path))

    pages_text = []

    for page in reader.pages:
        text = page.extract_text()

        if text:
            pages_text.append(text)

    return "\n".join(pages_text)