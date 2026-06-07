from sentence_transformers import SentenceTransformer # type: ignore
from app.config import get_settings

settings = get_settings()

class Embedder:
    def __init__(self):
        self.model = SentenceTransformer(settings.embedding_model)

    def embed_chunks(self, chunks: list[dict]) -> list[dict]:
        """
        input:  [{"text": "...", "page_number": 1, "chunk_index": 0}, ...]
        output: [{"text": "...", "page_number": 1, "chunk_index": 0, "embedding": [...]}, ...]
        """
        texts = [chunk["text"] for chunk in chunks]
        embeddings = self.model.encode(texts, show_progress_bar=True)

        for chunk, embedding in zip(chunks, embeddings):
            chunk["embedding"] = embedding.tolist()  

        return chunks
    def embed_text(self , query :str ) -> list[float] : 
        return self.model.encode(query).tolist()
    