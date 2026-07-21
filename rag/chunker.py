"""
MedRAG AI
Phase 4 - Document Chunking
"""

from pathlib import Path
import json


def chunk_text(text, chunk_size=500, overlap=100):
    """
    Split text into overlapping chunks.
    """

    chunks = []

    start = 0

    while start < len(text):

        end = start + chunk_size

        chunk = text[start:end]

        chunks.append(chunk)

        start += chunk_size - overlap

    return chunks


def chunk_document(json_path: Path):

    with open(json_path, "r", encoding="utf-8") as f:
        document = json.load(f)

    text = document["text"]

    chunks = chunk_text(text)

    output = []

    for i, chunk in enumerate(chunks):

        output.append(
            {
                "chunk_id": i,
                "filename": document["filename"],
                "text": chunk,
            }
        )

    return output