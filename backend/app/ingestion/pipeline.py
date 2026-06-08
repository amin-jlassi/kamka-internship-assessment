from app.utils.pdf_parser import PDFParser
from app.ingestion.chunker import Chunker
from app.ingestion.embedder import Embedder
from app.vectoreStore.chroma import VectorStore

"""
Pipeline class orchestrates the entire RAG process:
1. Ingestion:
    - Determines file type (PDF or TXT) and extracts text with metadata.
    - Chunks the text while preserving page number metadata.
    - Generates embeddings for each chunk.
    - Stores chunks and embeddings in the vector database.
2. Querying:
    - Embeds the input query.
    - Retrieves relevant chunks from the vector database based on embedding similarity.
"""


class Pipeline : 
    def __init__(self) :
        self.pdfParser = PDFParser()
        self.chunker = Chunker()
        self.embedder = Embedder()
        self.vectorStore = VectorStore()
    def ingest(self , file_path : str) -> dict : 
        extension = file_path.split(".")[-1]
        filename = file_path.split("\\")[-1]
        print(f"ingesting file : {filename} with extension : {extension}")
        if extension == "pdf" :
            data = self.pdfParser.extract_text_with_metadata(file_path)
        elif extension == "txt" :
            f = open(file_path , "r")
            text = f.read()
            data = [{"text" : text , "page_number" : 1}]
            f.close()
        else :
            raise ValueError(f"unsupported file type: {extension}")
        chunks = self.chunker.chunk_text_with_metadata(data)
        embedded_chunks = self.embedder.embed_chunks(chunks)
        self.vectorStore.add_embeddings(filename , embedded_chunks)
        return {"message": "ingestion completed" , "filename": filename , "num_chunks": len(chunks)}
    def query(self , query : str) -> list[dict] :
        query_embedding = self.embedder.embed_text(query)
        chunks = self.vectorStore.retrieve_related_chunks(query_embedding)
        return chunks
        