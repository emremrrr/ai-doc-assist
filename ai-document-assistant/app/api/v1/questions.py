from fastapi import APIRouter,Query
from pydantic import BaseModel

from app.services.vector_store_service import search_relevant_chunks
from app.services.llm_service import generate_answer

router = APIRouter()


class AskQuestionRequest(BaseModel):
    question: str
    max_results: int = 3


@router.get("")
async def ask_question(
    question: str = Query(..., min_length=1),
    max_results: int = Query(3, ge=1, le=10)
):
    matches = search_relevant_chunks(
        question=question,
        max_results=max_results
    )

    answer = generate_answer(
        question=question,
        context_chunks=matches
    )

    sources = [
        match["metadata"] for match in matches
    ]

    return {
        "question": question,
        "answer": answer,
        "sources": sources
    }