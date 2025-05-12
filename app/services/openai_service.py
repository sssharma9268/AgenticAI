import os
from typing import Any

from dotenv import load_dotenv
from openai import AsyncOpenAI

load_dotenv()


class OpenAIService:
    """Service class for handling OpenAI API interactions."""

    def __init__(self) -> None:
        """Initialize OpenAI client with API key from environment variables."""
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY environment variable is not set")

        self.client = AsyncOpenAI(api_key=api_key)
        self.model = "gpt-3.5-turbo"

    async def get_chat_completion(self, prompt: str) -> dict[str, Any]:
        """
        Get chat completion from OpenAI API.

        Args:
            prompt (str): The user's input prompt

        Returns:
            dict[str, Any]: Response containing status and either the completion or error
        """
        try:
            response = await self.client.chat.completions.create(
                model=self.model, messages=[{"role": "user", "content": prompt}]
            )

            return {
                "status": "success",
                "response": response.choices[0].message.content,
                "model": self.model,
            }

        except Exception as e:
            return {"status": "error", "error": str(e)}
