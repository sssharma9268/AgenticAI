from typing import Any

from fastapi import APIRouter

from app.generic_constants import APP_VERSION

version_router = APIRouter()


@version_router.get("/api/version")
async def get_version() -> dict[str, Any]:
    """
    Get the version of the API
    """
    return {
        "version": APP_VERSION,
    }
