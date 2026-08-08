from google.genai import types

from models import gemini_client
from schemas import ExtractedDataSummary
from .base import LLMProvider


class GeminiProvider(LLMProvider):

    def generate(self, prompt: str) -> str:
        response = gemini_client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=ExtractedDataSummary,
            ),
        )

        return response.text.strip()