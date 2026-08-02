from app.services.embedding_service import EmbeddingService
from app.services.vector_service import VectorService


class SearchService:

    @staticmethod
    def search_chunks(question: str):

        embedding = EmbeddingService.generate_embedding(
            question
        )

        results = VectorService.search(
            embedding=embedding,
            n_results=3
        )

        return results