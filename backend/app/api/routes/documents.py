from fastapi import APIRouter, UploadFile, File, HTTPException #type: ignore
from pathlib import Path
import shutil

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

router = APIRouter()

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

    return {
        "message": "File uploaded successfully",
        "filename": file.filename
    }


@router.get("/files")
def list_files():
    files = [f.name for f in UPLOAD_DIR.iterdir() if f.is_file()]
    return {"files": files}