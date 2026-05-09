from fastapi import APIRouter, UploadFile, File, HTTPException
from pathlib import Path
from app.services.text_extractor import extract_text

router = APIRouter()

ALLOWED_CONTENT_TYPES = {
    "application/pdf",
    "text/plain"
}

UPLOAD_DIR=Path("docs")
UPLOAD_DIR.mkdir(exist_ok=True)

@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    print('upload begin')
    if file.content_type not in ALLOWED_CONTENT_TYPES:
        raise HTTPException(
            status_code=400,
            detail="Only PDF and TXT files are allowed."
        )
    file_path=UPLOAD_DIR / file.filename
    content=await file.read()

    with open(file_path, "wb") as f:
        f.write(content)
    
    extracted_text = extract_text(str(file_path))

    return {
        "file_name": file.filename,
        "content_type": file.content_type,
        "size_bytes": len(content),
        "saved_path": str(file_path),
        "extracted_text_preview": extracted_text[:500],
        "status": "uploaded"
    }


@router.get("/")
def get_documents():
    return {
        "documents": []
    }