from typing import Any, Callable

from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import Response

from app.common import settings
from app.routes import all_api_routes

app = FastAPI(
    title="Agentic AI Platform APIs",
    description="APIs for interacting with Agentic AI Platform",
    docs_url="/swagger",
    swagger_ui_parameters={"tryItOutEnabled": True},
)

app.include_router(all_api_routes)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UNPROTECTED_ROUTES = [
    "/api/health",
    "/api/version",
    "/swagger",
    "/redoc",
    "/openapi.json",
    "/swagger/oauth2-redirect",
]


@app.middleware("http")
async def authentication(request: Request, call_next: Callable[[Request], Any]) -> Response:
    if request.url.path in UNPROTECTED_ROUTES:
        unprotected_response: Response = await call_next(request)
        return unprotected_response

    request_api_key = request.headers.get("api-key")
    request_app_id = request.headers.get("app-id")

    if request_api_key != settings.API_KEY or request_app_id != settings.APP_ID:
        raise HTTPException(status_code=401, detail="Unauthorized")

    response: Response = await call_next(request)
    return response
