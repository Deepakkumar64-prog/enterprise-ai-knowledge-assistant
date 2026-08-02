from fastapi import APIRouter

from app.schemas.chat import ChatRequest
from app.services.llm_service import LLMService

router = APIRouter()


@router.post("/chat")
def chat(request: ChatRequest):

    answer = LLMService.generate_response(
        request.question
    )

    return {
        "success": True,
        "question": request.question,
        "answer": answer
    }