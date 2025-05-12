from .all_routes import all_api_routes
from .chat_completion_routes import chat_completion_router
from .health_routes import health_router
from .version_routes import version_router

__all__ = ["version_router", "health_router", "chat_completion_router", "all_api_routes"]
