import os
import json

from pydantic import BaseModel
from google import genai

client  = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# class SummaryResponse(BaseModel):
#     summary:str
#     sentiment:str
#     keywords:list[str]

class EntityExtraction(BaseModel):
    names:list[str]
    dates:list[str]
    locations:list[str]

# prompt1 = """
# Summarize the following text.

# Text:
# Python is one of the most popular programming languages for AI development.

# Return ONLY valid JSON in this format:

# {
#   "summary":"",
#   "sentiment":"",
#   "keywords":[]
# }
# """

input_text = input("Enter the text to extract data: ")

entity_extraction_prompt = f"""
You are an information extraction system.

Extract all person names, dates, and locations from the text.
Preserve honorifics such as Dr., Professor, Mr., Ms., etc., exactly as they appear in the text.

Return ONLY valid JSON.

Do NOT explain anything.
Do NOT summarize.
Do NOT use markdown.
Do NOT add extra text.

The JSON must exactly match this schema:

{{
    "names": [],
    "dates": [],
    "locations": []
}}

Text:
{input_text}
"""

# response1 = client.models.generate_content(
#     model="gemini-3-flash-preview",
#     contents=prompt1
# )

extracted_entities = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=entity_extraction_prompt
)

# print(response2.text)
extracted_text = extracted_entities.text.strip()

extracted_data = json.loads(extracted_text)

# validated = SummaryResponse.model_validate(data)

entity_extracted_validated = EntityExtraction.model_validate(extracted_data)


print(entity_extracted_validated.model_dump_json(indent=4))