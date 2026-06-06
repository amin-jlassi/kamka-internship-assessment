from fastapi import FastAPI  # type: ignore
from app.config import get_settings  

app = FastAPI()
settings = get_settings()

@app.get("/")
def read_root():
    return {"Hello": "World"}
