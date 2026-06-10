# app/agent/llm.py
from app.config import get_settings
from app.agent.db.models import get_llm_provider

settings = get_settings()

def extract_content(response) -> str:
    content = response.content
    if isinstance(content, list):
        content = content[0]["text"] if isinstance(content[0], dict) else content[0]
    return content.strip()

def get_llm(streaming: bool = False):
    provider = get_llm_provider() or settings.llm_provider
    print(f"using provider: {provider}")

    if provider == "google":
        from langchain_google_genai import ChatGoogleGenerativeAI # type: ignore
        return ChatGoogleGenerativeAI(
            model=settings.model_name,
            temperature=0,
            api_key=settings.google_api_key,
            streaming=streaming
        )
    elif provider == "ollama":
        from langchain_ollama import ChatOllama # type: ignore
        return ChatOllama(
            model=settings.ollama_model_name,
            base_url=settings.ollama_host,
            temperature=0,
            streaming=streaming
        )
    else:
        raise ValueError(f"Unsupported provider: {provider}")