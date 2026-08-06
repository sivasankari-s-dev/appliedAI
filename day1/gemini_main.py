import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

prompt = input("What is your question? : ")

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=prompt
)

print("Gemini says..")
print(response.text)