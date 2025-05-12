# Routes for the API

from fastapi import APIRouter

from app.routes import chat_completion_routes, health_routes, version_routes

all_api_routes = APIRouter()

all_api_routes.include_router(health_routes.health_router, tags=["Health"])
all_api_routes.include_router(version_routes.version_router, tags=["Version"])
all_api_routes.include_router(
    chat_completion_routes.chat_completion_router, tags=["Chat Completion"]
)
