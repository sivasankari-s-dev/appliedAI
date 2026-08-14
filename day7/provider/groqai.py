
import os

from groq import Groq

groqai_client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_response(prompt: str) -> str:
    response = groqai_client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
    )
    return response.choices[0].message.content.strip()