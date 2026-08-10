from models import groq_client

from schemas import CustomerTicket
from .base import LLMProvider

class GroqProvider(LLMProvider):

    def generate(self, prompt: str) -> str:
        response = groq_client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                 {
                    "role": "system",
                    "content":  "Return only valid JSON."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            response_format={
                "type": "json_object",
            }
        )
        return response.choices[0].message.content.strip()