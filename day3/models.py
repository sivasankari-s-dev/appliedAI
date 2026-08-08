import os

from google import genai
from google.genai import types

# Gemini Model Client
gemini_client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))



