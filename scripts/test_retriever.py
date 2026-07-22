"""
Test MedRAG AI Retrieval
"""

from rag.retriever import Retriever


def main():

    retriever = Retriever()

    question = input("Question: ")

    results = retriever.search(question)

    print("=" * 60)

    docs = results["documents"][0]
    metas = results["metadatas"][0]

    for i, (doc, meta) in enumerate(zip(docs, metas), start=1):

        print(f"\nResult {i}")
        print("-" * 60)
        print(f"Source : {meta['filename']}")
        print(f"Chunk  : {meta['chunk_id']}")
        print()
        print(doc[:700])
        print()


if __name__ == "__main__":
    main()