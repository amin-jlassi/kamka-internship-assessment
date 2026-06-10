from functools import lru_cache
from app.config import get_settings

settings = get_settings()

current_provider = {"name": settings.llm_provider}  # default from .env
def set_provider(model_name: str):
    if "gemini" in model_name.lower():
        current_provider["name"] = "google"
    elif "mistral" in model_name.lower():
        current_provider["name"] = "ollama"
    else:
        raise ValueError(f"Unsupported model: {model_name}")
    
    

def extract_content(response) -> str:
    content = response.content
    if isinstance(content, list):
        content = content[0]["text"] if isinstance(content[0], dict) else content[0]
    return content.strip()
    
@lru_cache()
def get_llm():
    print(current_provider)
    if current_provider['name'] == "google":
        from langchain_google_genai import ChatGoogleGenerativeAI #type: ignore
        return ChatGoogleGenerativeAI(model=settings.model_name, temperature=0 , api_key=settings.google_api_key , streaming = True)
    
    elif current_provider["name"] == "ollama":
        from langchain_ollama import ChatOllama #type: ignore
        return ChatOllama(
            model=settings.ollama_model_name,
            base_url=settings.ollama_host,
            temperature=0 , 
            streaming = True ,
        )
        
    
    else:
        raise ValueError(f"Unsupported LLM provider: {settings.llm_provider}")