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
    k_index: int = 5
    
    
    #llm provider
    
    llm_provider: str = "ollama"  
    
    #google
    google_api_key: str 
    model_name: str = "gemini-3.5-flash"
    
    #ollama
    ollama_host: str = "http://localhost:11434"
    ollama_model_name: str = "mistral"
    
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"
        

        
        
@lru_cache()
def get_settings():
    return Settings()