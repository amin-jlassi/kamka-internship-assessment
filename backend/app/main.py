from fastapi import FastAPI  # type: ignore
from app.config import get_settings  
from app.api.routes.documents import router as documents_router
from app.api.routes.chat import router as chat_router
from app.api.routes.llm import router as llm_router
from fastapi.middleware.cors import CORSMiddleware  # type: ignore
app = FastAPI()
origins = [
    "http://localhost:3000",  
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(documents_router)
app.include_router(chat_router)
app.include_router(llm_router)
settings = get_settings()

@app.get("/")
def read_root():
    return {"Hello": "World"}
