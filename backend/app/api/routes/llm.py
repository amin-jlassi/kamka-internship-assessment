from fastapi import APIRouter, HTTPException, status # type: ignore
from pydantic import BaseModel # type: ignore
from app.agent.llm import set_provider

router = APIRouter()

class LlmRequest(BaseModel):
    model_name: str

@router.post("/llm", status_code=status.HTTP_200_OK)
async def switch_llm(request: LlmRequest):
    try:
        set_provider(request.model_name)
        return {"model": request.model_name, "status": "switched"}
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )