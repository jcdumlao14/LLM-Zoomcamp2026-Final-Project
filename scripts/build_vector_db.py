import json
from pathlib import Path

from rag.embedding import EmbeddingModel
from rag.vector_store import collection

DATA_DIR = Path("data/chunks")

embedder = EmbeddingModel()


def main():

    total = 0

    for file in DATA_DIR.glob("*.json"):

        with open(file, "r", encoding="utf-8") as f:
            chunks = json.load(f)

        # Skip empty chunk files
        if len(chunks) == 0:
            print(f"Skipping {file.name} (no chunks found)")
            continue

        texts = [c["text"] for c in chunks]

        # Skip if all texts are empty
        if len(texts) == 0:
            print(f"Skipping {file.name} (no text found)")
            continue

        embeddings = embedder.encode(texts)

        ids = []
        metadatas = []

        for c in chunks:

            ids.append(
                f"{c['filename']}_{c['chunk_id']}"
            )

            metadatas.append(
                {
                    "filename": c["filename"],
                    "chunk_id": c["chunk_id"]
                }
            )

        collection.add(
            ids=ids,
            embeddings=embeddings.tolist(),
            documents=texts,
            metadatas=metadatas
        )

        print(f"Indexed {file.name}")

        total += len(texts)

    print("-" * 50)
    print(f"Total indexed chunks: {total}")


if __name__ == "__main__":
    main()