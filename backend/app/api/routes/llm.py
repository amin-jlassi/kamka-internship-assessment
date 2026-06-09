from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

from app.config import get_settings

settings = get_settings()
router = APIRouter()


class LlmRequest(BaseModel):
    model_name: str


@router.post("/llm", status_code=status.HTTP_200_OK)
async def chat(request: LlmRequest):
    
    if request.model_name == "gemini-3.5-flash":
        settings.model_name = "gemini-3.5-flash"

    elif "Mistral" in request.model_name :
        settings.model_name = "mistral"

    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Unsupported model"
        )

    return {
        "model": settings.model_name
    }