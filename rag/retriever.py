"""
MedRAG AI
Phase 6 - Semantic Retriever
"""

from rag.embedding import EmbeddingModel
from rag.vector_store import collection

embedder = EmbeddingModel()


def search(query, k=5):
    """
    Semantic search over ChromaDB.
    """

    query_embedding = embedder.encode([query])[0]

    results = collection.query(
        query_embeddings=[query_embedding.tolist()],
        n_results=k
    )

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]
    distances = results["distances"][0]

    output = []

    for doc, meta, dist in zip(documents, metadatas, distances):
        output.append({
            "text": doc,
            "filename": meta["filename"],
            "chunk_id": meta["chunk_id"],
            "distance": dist,
        })

    return output