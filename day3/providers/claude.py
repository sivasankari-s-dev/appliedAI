from models import claude_client

from .base import LLMProvider


class ClaudeProvider(LLMProvider):

    def generate(self, prompt: str) -> str:
        response = claude_client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=2048,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        return response.content[0].text