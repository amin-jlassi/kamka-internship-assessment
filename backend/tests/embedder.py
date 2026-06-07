import sys
sys.path.append(".")
from app.utils.pdf_parser import PDFParser
from app.ingestion.chunker import Chunker
from app.ingestion.embedder import Embedder
from app.vectoreStore.chroma import VectorStore

#text = PDFParser("uploads/liste_chaine.pdf").extract_text_with_metadata()
chunker = Chunker()
#chunks = chunker.chunk_text_with_metadata(text)
embedder = Embedder()
#embedded_chunks = embedder.embed_chunks(chunks)
print(embedder.embed_text("hello"))