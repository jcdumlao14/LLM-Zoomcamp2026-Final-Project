"""
MedRAG AI
Phase 3 - PDF Ingestion Pipeline
"""

import json
from pathlib import Path

import fitz


RAW_DIR = Path("data/raw")
PROCESSED_DIR = Path("data/processed")

PROCESSED_DIR.mkdir(parents=True, exist_ok=True)


def extract_pdf(pdf_path: Path) -> dict:
    """Extract metadata and text from a PDF."""

    pages = []
    full_text = ""

    with fitz.open(pdf_path) as document:

        metadata = document.metadata

        for page_number, page in enumerate(document, start=1):
            text = page.get_text()

            pages.append(
                {
                    "page": page_number,
                    "text": text,
                }
            )

            full_text += text + "\n"

    return {
        "filename": pdf_path.name,
        "title": metadata.get("title", ""),
        "author": metadata.get("author", ""),
        "pages": len(pages),
        "text": full_text,
        "page_content": pages,
    }


def save_document(document: dict):

    output_file = PROCESSED_DIR / f"{Path(document['filename']).stem}.json"

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(document, f, indent=2, ensure_ascii=False)


def main():

    pdf_files = sorted(RAW_DIR.glob("*.pdf"))

    if not pdf_files:
        print("No PDF files found inside data/raw/")
        return

    print("=" * 60)
    print("MedRAG AI")
    print("PDF Ingestion")
    print("=" * 60)

    for pdf in pdf_files:

        print(f"Processing: {pdf.name}")

        document = extract_pdf(pdf)

        save_document(document)

        print(f"Pages: {document['pages']}")
        print(f"Characters: {len(document['text']):,}")
        print("-" * 60)

    print("\nAll documents processed successfully.")


if __name__ == "__main__":
    main()
    