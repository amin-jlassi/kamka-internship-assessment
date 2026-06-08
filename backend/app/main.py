from fastapi import FastAPI  # type: ignore
from app.config import get_settings  
from app.api.routes.documents import router as documents_router
from app.api.routes.chat import router as chat_router

app = FastAPI()
app.include_router(documents_router)
app.include_router(chat_router)
settings = get_settings()

@app.get("/")
def read_root():
    return {"Hello": "World"}
