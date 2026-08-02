import chromadb


class VectorService:

    client = chromadb.PersistentClient(
        path="./chroma_db"
    )

    collection = client.get_or_create_collection(
        name="enterprise_documents"
    )

    @classmethod
    def store_chunk(
        cls,
        chunk_id: str,
        chunk_text: str,
        embedding: list
    ):
        cls.collection.add(
            ids=[chunk_id],
            documents=[chunk_text],
            embeddings=[embedding]
        )

    @classmethod
    def search(
        cls,
        embedding: list,
        n_results: int = 3
    ):
        return cls.collection.query(
            query_embeddings=[embedding],
            n_results=n_results
        )