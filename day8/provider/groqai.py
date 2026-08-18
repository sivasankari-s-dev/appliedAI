from groq import Groq
import os

groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_response(prompt: str) -> str:
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
        # response_format={
        #     "type": "json_object",
        # }
    )
    return response.choices[0].message.content.strip()