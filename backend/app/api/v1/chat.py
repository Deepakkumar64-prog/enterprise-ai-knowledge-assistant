from fastapi import APIRouter

from app.schemas.chat import ChatRequest

router = APIRouter()


@router.post("/chat")
def chat(request: ChatRequest):
    return {
        "success": True,
        "question": request.question,
        "answer": f"You asked: {request.question}"
    }