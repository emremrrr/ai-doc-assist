from fastapi import APIRouter, UploadFile, File, HTTPException
from pathlib import Path
from app.services.text_extractor import extract_text
from app.services.vector_store_service import store_chunks
from app.services.chunking_service import split_text_into_chunks

router = APIRouter()

ALLOWED_CONTENT_TYPES = {
    "application/pdf",
    "text/plain"
}

UPLOAD_DIR=Path("docs")
UPLOAD_DIR.mkdir(exist_ok=True)

@router.post("")
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
    chunks = split_text_into_chunks(extracted_text)
    stored_chunk_count = store_chunks(file.filename, chunks)
    return {
        "file_name": file.filename,
        "content_type": file.content_type,
        "size_bytes": len(content),
        "saved_path": str(file_path),
        "extracted_text_preview": extracted_text[:500],
        "chunk_count": len(chunks),
        "first_chunk_preview": chunks[0][:300] if chunks else None,
        "status": "uploaded"
    }


@router.get("")
def get_documents():
    docs = []

    for file in UPLOAD_DIR.iterdir():
        if file.is_file():
            docs.append({
                "file_name": file.name,
                "size_bytes": file.stat().st_size,
                "path": str(file)
            })

    return {
        "docs": docs
    }