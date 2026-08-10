from models import groq_client

from schemas import ExtractedDataSummary
from .base import LLMProvider

class GroqProvider(LLMProvider):

    def generate(self, prompt: str) -> str:
        response = groq_client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                 {
                    "role": "system",
                    "content": f"Return the response as valid JSON in format: {ExtractedDataSummary.model_json_schema()}"
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            response_format={
                "type": "json_object",
                # "json_schema": {
                #     "name": "extracted_data_summary",
                #     "schema": ExtractedDataSummary.model_json_schema()
                #     }
            }
        )
        return response.choices[0].message.content.strip()