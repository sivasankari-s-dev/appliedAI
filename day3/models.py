import os

from google import genai
from anthropic import Anthropic

# Gemini Model Client
gemini_client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

claude_client = Anthropic(
    api_key=os.getenv("CLAUDE_API_KEY")
)



