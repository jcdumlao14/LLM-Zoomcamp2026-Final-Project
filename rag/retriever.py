"""
MedRAG AI
Phase 6 - Semantic Retriever
"""

from rag.embedding import EmbeddingModel
from rag.vector_store import collection


class Retriever:

    def __init__(self):

        self.embedder = EmbeddingModel()

    def search(self, query, top_k=5):

        query_embedding = self.embedder.encode([query])[0]

        results = collection.query(
            query_embeddings=[query_embedding.tolist()],
            n_results=top_k
        )

        return results