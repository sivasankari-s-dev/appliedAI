import os

from google import genai
from groq import Groq

# Gemini Model Client
gemini_client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


groq_client = Groq(
    api_key=os.getenv("GROQ_API_KEY"))



