from fastapi import FastAPI

from app.api.v1.health import router as health_router
from app.api.v1.chat import router as chat_router
from app.api.v1.documents import router as document_router
from app.api.v1.rag import router as rag_router
from app.config.settings import settings

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)

# Health APIs
app.include_router(
    health_router,
    prefix="/api/v1",
    tags=["Health"]
)

# Chat APIs
app.include_router(
    chat_router,
    prefix="/api/v1",
    tags=["Chat"]
)

# Document APIs
app.include_router(
    document_router,
    prefix="/api/v1",
    tags=["Documents"]
)

# RAG APIs
app.include_router(
    rag_router,
    prefix="/api/v1",
    tags=["RAG"]
)