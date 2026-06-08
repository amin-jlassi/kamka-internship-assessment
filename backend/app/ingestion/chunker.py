from langchain_text_splitters import RecursiveCharacterTextSplitter # type: ignore
from app.config import get_settings

"""
Chunker class for splitting text into manageable chunks while preserving metadata.
- Uses RecursiveCharacterTextSplitter from langchain_text_splitters.
- Configured with chunk size and overlap from application settings.
- Provides methods for chunking plain text and page-aware content with metadata.


"""



settings = get_settings()

class Chunker:
    def __init__(self):
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=settings.chunk_size,
            chunk_overlap=settings.chunk_overlap
        )

    def chunk_text(self, text: str) -> list[str]:
        """Chunk a plain string."""
        return self.splitter.split_text(text)

    def chunk_text_with_metadata(self, pages: list[dict]) -> list[dict]:
        """
        Chunk page-aware content, preserving page number metadata.
        Input:  [{"text": "...", "page_number": 1}, ...]
        Output: [{"text": "...", "page_number": 1, "chunk_index": 0}, ...]
        """
        chunks = []
        for page in pages:
            page_chunks = self.splitter.split_text(page["text"])
            for i, chunk in enumerate(page_chunks):
                chunks.append({
                    "text": chunk,
                    "page_number": page["page_number"],
                    "chunk_index": i
                })
        return chunks