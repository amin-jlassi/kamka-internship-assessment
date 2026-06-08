from fastapi import APIRouter, UploadFile, File, HTTPException #type: ignore
from pathlib import Path
import shutil
from app.ingestion.pipeline import Pipeline 
import os


"""

API routes for document management:
- POST /upload: Endpoint for uploading PDF and TXT files. Validates file type, saves
the file, and triggers the ingestion pipeline. Handles errors gracefully.
- GET /files: Endpoint to list all uploaded files in the uploads directory.

"""




UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

router = APIRouter()
pipeline = Pipeline()

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    allowed_types = {
        "application/pdf",
        "text/plain"
    }

    if file.content_type not in allowed_types:
        raise HTTPException(
            status_code=400,
            detail="Only PDF and TXT files are allowed"
        )

    file_path = UPLOAD_DIR / file.filename

    with file_path.open("wb") as copied_file:
        shutil.copyfileobj(file.file, copied_file)
    
    
    try:
        print(f"ingesting file : {file_path}")
        result = pipeline.ingest(str(file_path))
    except Exception as e:
        os.remove(file_path)
        raise HTTPException(status_code=500, detail=str(e))
    else:
        return {
            "message": "File uploaded successfully",
            "filename": file.filename
        }


@router.get("/files")
def list_files():
    files = [f.name for f in UPLOAD_DIR.iterdir() if f.is_file()]
    return {"files": files}