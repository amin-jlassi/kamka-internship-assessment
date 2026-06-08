import chromadb  # type: ignore
from app.config import get_settings 
import uuid 




"""

docs : 

VectorStore Class contains the methods which they will be used in the rag pipleline  : 
- add_embeddings method : used for storing embeddings into chroma database . 
params : filename (pdf name) / chunks :  list of dictionnarys with this expected format [{"text": "...", "page_number": 1, "chunk_index": 0, "embedding": [...]}, ...] 
it returns Nothing

- retrieve_chunks method : used for retievig the most related k chunks to the given query 
params : query_embedding : the main query formated into embeddings
it returns a list of dictionnarys which are the chunks which context is similar to the question and their metadata

output : [{"text": "...", "metadata" :{"filename" : "...","page_number": 1, "chunk_index": 0,} , "score": 1.0 }, ...]

- get_document_chunks_by_filename method : used for retrieving all the chunks of a document using its filename
params : filename : the name of the document (pdf)
it returns a list of dictionnarys which are the chunks of the document and their metadata
output : [{"text": "...", "metadata" :{"filename" : "...","page_number": 1, "chunk_index": 0,} }, ...]

"""


settings = get_settings()
class VectorStore : 
    def __init__(self):
        self.client = chromadb.PersistentClient(path=settings.chroma_database_folder_location)
        self.collection = self.client.get_or_create_collection(name=settings.chroma_collection_name)
    def add_embeddings(self, filename : str ,  chunks: list[dict]) -> None :
        "store chunks and  embeddings with their metadata in the database"
        self.collection.add(
            ids = [str(uuid.uuid4())  for _ in chunks] , 
            embeddings =[chunk["embedding"] for chunk in chunks] , 
            documents  = [chunk["text"] for chunk in chunks] , 
            metadatas = [{
                "filename" : filename , 
                "page_number" : chunk["page_number"] , 
                "chunk_index" : chunk["chunk_index"] 
            } for chunk in chunks]
        )
    def retrieve_related_chunks(self , query_embedding : list[float]) -> list[dict] :
        """retrieve chunks that are relative the question (query)"""
        k = settings.k_index
        res = self.collection.query(
            query_embeddings = [query_embedding],
            n_results = k , 
            include = ["documents", "metadatas" , "distances"]
        )
        chunks = []
        for text , metadata , distance in zip(res["documents"][0] , res["metadatas"][0] , res["distances"][0]) : 
            chunks.append({
                    "text" : text , 
                    "metadata" : metadata , 
                    "score" : round(1-distance , 3) 
            })
        
        return chunks
    def get_document_chunks_by_filename(self , filename : str) -> list[dict] :
        """retrieve all the chunks of a document using its filename"""
        res = self.collection.query(
            include = ["documents", "metadatas" , "distances"] , 
            where = {"filename" : filename}
        )
        chunks = []
        for text , metadata in zip(res["documents"][0] , res["metadatas"][0]) : 
            chunks.append({
                    "text" : text , 
                    "metadata" : metadata
            })
        
        return chunks
        
        