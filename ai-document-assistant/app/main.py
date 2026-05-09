from fastapi import FastAPI
from app.api.v1 import health
from app.api.v1 import documents

app = FastAPI(
    title="AI Document Assistant",
    version="1.0.0"
)

app.include_router(health.router, prefix="/api/v1", tags=["Health"])
app.include_router(documents.router, prefix="/api/v1/documents", tags=["Documents"])