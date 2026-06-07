from pydantic_settings import BaseSettings  # type: ignore
from functools import lru_cache  # type: ignore


class Settings(BaseSettings):
    
    #chunking
    chunk_size: int = 800
    chunk_overlap: int = 150
    
    #embedding
    embedding_model: str = "all-MiniLM-L6-v2"
    
    # chromadb
    chroma_database_folder_location: str = "./chroma_db"
    chroma_collection_name: str = "documents"
    k_index = 5
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        
        
@lru_cache()
def get_settings():
    return Settings()