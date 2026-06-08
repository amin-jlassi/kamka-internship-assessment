from fastapi import APIRouter, HTTPException # type: ignore
from pydantic import BaseModel # type: ignore
from app.agent.graph import agent
from app.agent.state import AgentState

router = APIRouter()

class ChatRequest(BaseModel):
    query: str
    filename: str | None = None

class ChatResponse(BaseModel):
    answer: str
    sources: list[dict]

@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
        state = AgentState(
            query=request.query,
            tool="",
            context=[],
            answer="",
            filename=request.filename
        )

        result = agent.invoke(state)

        return ChatResponse(
            answer=result["answer"],
            sources=result["context"]
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))