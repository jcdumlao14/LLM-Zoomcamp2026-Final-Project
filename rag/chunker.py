"""
MedRAG AI
Document Chunker
"""

import json
from pathlib import Path


# Chunk configuration
CHUNK_SIZE = 1200        # characters
CHUNK_OVERLAP = 200      # characters


def chunk_text(text, chunk_size=CHUNK_SIZE, overlap=CHUNK_OVERLAP):
    """
    Split text into overlapping chunks.
    """

    if not text:
        return []

    chunks = []

    start = 0
    text_length = len(text)

    while start < text_length:

        end = min(start + chunk_size, text_length)

        chunk = text[start:end].strip()

        if chunk:
            chunks.append(chunk)

        if end == text_length:
            break

        start = end - overlap

    return chunks


def chunk_document(json_file: Path):
    """
    Chunk one processed document.
    """

    with open(json_file, "r", encoding="utf-8") as f:
        document = json.load(f)

    # Extract filename
    filename = document.get("filename", json_file.with_suffix(".pdf").name)

    # Extract text
    text = document.get("text", "")

    if not text.strip():
        return []

    text_chunks = chunk_text(text)

    output = []

    for i, chunk in enumerate(text_chunks):

        output.append(
            {
                "filename": filename,
                "chunk_id": i,
                "text": chunk,
            }
        )

    return output