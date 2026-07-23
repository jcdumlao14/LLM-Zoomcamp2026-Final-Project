"""
Test MedRAG AI Retrieval
"""

from rag.retriever import search


def main():
    query = input("Question: ")

    results = search(query, k=5)

    print("=" * 60)

    for i, result in enumerate(results, 1):
        print(f"\nResult {i}")
        print("-" * 60)
        print("Source :", result["filename"])
        print("Chunk  :", result["chunk_id"])
        print("Score  :", round(result["distance"], 4))
        print()
        print(result["text"][:600])


if __name__ == "__main__":
    main()
    