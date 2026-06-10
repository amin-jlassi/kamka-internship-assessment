from fastapi import APIRouter, HTTPException, status # type: ignore
from pydantic import BaseModel # type: ignore
from app.agent.db.models import update_llm_provider , get_llm_provider

router = APIRouter()

class LlmRequest(BaseModel):
    model_name: str

@router.post("/llm", status_code=status.HTTP_200_OK)
async def switch_llm(request: LlmRequest):
    try:
        model_name = request.model_name
        if "gemini" in model_name.lower() : 
            model_name = "google"
        elif "mistral" in model_name.lower() : 
            model_name = "ollama"
        update_llm_provider(model_name)
        return {"model": model_name, "status": "switched"}
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
@router.get("/llm", status_code=status.HTTP_200_OK)
async def get_llm():
    try:
        model_name = get_llm_provider()
        return {"model": model_name,}
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
