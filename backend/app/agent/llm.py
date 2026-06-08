from app.config import get_settings

settings = get_settings()


def get_llm():
    if settings.llm_provider == "google":
        from langchain_google_genai import ChatGoogleGenerativeAI #type: ignore
        return ChatGoogleGenerativeAI(model=settings.model_name, temperature=0 , api_key=settings.google_api_key)
    
    elif settings.llm_provider == "ollama":
        from langchain_ollama import ChatOllama #type: ignore
        return ChatOllama(
            model=settings.ollama_model_name,
            base_url=settings.ollama_host,
            temperature=0
        )
    
    else:
        raise ValueError(f"Unsupported LLM provider: {settings.llm_provider}")