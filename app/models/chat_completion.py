from pydantic import BaseModel


class ChatRequest(BaseModel):
    prompt: str

    class Config:
        json_schema_extra = {"example": {"prompt": "What is the capital of France?"}}


class ChatResponse(BaseModel):
    status: str
    response: str | None = None
    model: str | None = None
    error: str | None = None
