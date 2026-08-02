from fastapi import FastAPI

from app.api.v1.health import router as health_router
from app.api.v1.chat import router as chat_router
from app.api.v1.documents import router as document_router
from app.config.settings import settings

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)

app.include_router(
    health_router,
    prefix="/api/v1",
    tags=["Health"]
)

app.include_router(
    chat_router,
    prefix="/api/v1",
    tags=["Chat"]
)

app.include_router(
    document_router,
    prefix="/api/v1",
    tags=["Documents"]
)