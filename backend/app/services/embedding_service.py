class EmbeddingService:

    @staticmethod
    def generate_embedding(text: str):
        return {
            "status": "success",
            "text_length": len(text)
        }