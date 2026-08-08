import json

from prompts import entity_extraction_prompt
from schemas import ExtractedDataSummary
from models import gemini_client, types

def generate_response(prompt: str) -> str:
    extracted_summarized_data = gemini_client.models.generate_content(
     model="gemini-3-flash-preview",
     contents=prompt,
     config=types.GenerateContentConfig(
          response_mime_type="application/json",
          response_schema=ExtractedDataSummary,
     ),
)
    return extracted_summarized_data.text.strip()

input_text = input("Enter the text : \n")
print()
print("-------------------------------------------------------------------------------------------")

prompt = f"""
{entity_extraction_prompt}
Text:
{input_text}
"""

extracted_text = generate_response(prompt)
print(extracted_text)

extracted_data_json = json.loads(extracted_text)

extracted_validated_summary = ExtractedDataSummary.model_validate(extracted_data_json)

print(extracted_validated_summary.model_dump_json(indent=4))