"""
Chunk all processed documents.
"""

import json
from pathlib import Path

from rag.chunker import chunk_document

INPUT_DIR = Path("data/processed")
OUTPUT_DIR = Path("data/chunks")

OUTPUT_DIR.mkdir(exist_ok=True)


def main():

    json_files = INPUT_DIR.glob("*.json")

    total_chunks = 0

    for file in json_files:

        chunks = chunk_document(file)

        output_file = OUTPUT_DIR / file.name

        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(chunks, f, indent=2)

        print(f"{file.name}: {len(chunks)} chunks")

        total_chunks += len(chunks)

    print("-" * 50)
    print(f"Total chunks: {total_chunks}")


if __name__ == "__main__":
    main()