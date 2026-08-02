from fastapi import APIRouter

from app.schemas.chat import ChatRequest
from app.services.search_service import SearchService
from app.services.llm_service import LLMService

router = APIRouter()


@router.post("/rag/chat")
def rag_chat(request: ChatRequest):

    results = SearchService.search_chunks(
        request.question
    )

    documents = results.get("documents", [[]])[0]

    context = "\n\n".join(documents)

    prompt = f"""
Answer the question only from the provided context.

Context:
{context}

Question:
{request.question}

Answer:
"""

    answer = LLMService.generate_response(
        prompt
    )

    return {
        "question": request.question,
        "answer": answer
    }