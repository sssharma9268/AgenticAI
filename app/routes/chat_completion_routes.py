from typing import Any

from fastapi import APIRouter, HTTPException

from app.models import ChatRequest, ChatResponse
from app.services.openai_service import OpenAIService

chat_completion_router = APIRouter()


@chat_completion_router.post(
    "/api/chat",
    response_model=ChatResponse,
    summary="Get chat completion",
    description="Send a prompt to OpenAI and get a chat completion response",
)
async def chat_completion(request: ChatRequest) -> dict[str, Any]:
    openai_service = OpenAIService()
    response = await openai_service.get_chat_completion(request.prompt)

    if response["status"] == "error":
        raise HTTPException(status_code=500, detail=response["error"])

    return response
