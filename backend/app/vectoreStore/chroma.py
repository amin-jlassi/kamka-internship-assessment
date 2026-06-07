import chromadb  # type: ignore
from app.config import get_settings 
import uuid 

settings = get_settings()


class VectorStore : 
    def __init__(self):
        self.client = chromadb.Client()
        self.collection = self.client.get_or_create_collection(name=settings.chroma_collection_name)
    def add_embeddings(self, filename : str ,  chunks: list[dict]) -> None :
        "store chunks and  embeddings with their metadata in the database"
        self.collection.add(
            ids = [str(uuid.uuid4())  for _ in chunks] , 
            embeddings =[chunk["embeddings"] for chunk in chunks] , 
            documents  = [chunk["text"] for chunk in chunks] , 
            metadata = [{
                "filename" : filename , 
                "page_number" : chunk["page_number"] , 
                "chunk_index" : chunk["chunk_number"] 
            } for chunk in chunks]
        )
        
        