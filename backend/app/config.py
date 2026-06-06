from pydantic_settings import BaseSettings  # type: ignore
from functools import lru_cache  # type: ignore


class Settings(BaseSettings):
    
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        
        
@lru_cache()
def get_settings():
    return Settings()