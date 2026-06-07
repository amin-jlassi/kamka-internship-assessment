import sys
sys.path.append(".")
from app.utils.pdf_parser import PDFParser
from backend.app.ingestion.chunker import Chunker

text = PDFParser("uploads/plan_etude.pdf").extract_text_with_metadata()
chunker = Chunker()
chunks = chunker.chunk_text_with_metadata(text)
print(chunks)