from fastapi import FastAPI  # type: ignore
from app.config import get_settings  
from app.api.routes.documents import router as documents_router

app = FastAPI()
app.include_router(documents_router)
settings = get_settings()

@app.get("/")
def read_root():
    return {"Hello": "World"}
