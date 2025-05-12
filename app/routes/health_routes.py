from typing import Annotated, Any

from fastapi import APIRouter, Header

health_router = APIRouter()


@health_router.get("/api/health")
async def health_check(
    app_id: Annotated[str, Header()],
    api_key: Annotated[str, Header()],
) -> dict[str, Any]:
    """
    Health check for the API
    """
    return {
        "status": "ok",
        "app_id": app_id,
    }
