from groq import Groq
import os

groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_response(prompt: str) :
    response = groq_client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            # {
            #     "role": "system",
            #     "content": "Return only valid JSON."
            # },
            {
                "role": "user",
                "content": prompt
            }
        ],
        stream=True
    )
    for chunk in response:
        text = chunk.choices[0].delta.content
        if text:
            yield text