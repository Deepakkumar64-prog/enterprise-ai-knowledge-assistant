from fastapi import APIRouter

from app.config.settings import settings

router = APIRouter()


@router.get("/health")
def health():
    return {
        "success": True,
        "message": "Service is healthy",
        "data": {
            "app_name": settings.APP_NAME,
            "version": settings.APP_VERSION,
            "environment": settings.ENVIRONMENT
        }
    }