import os
import json

from google import genai
from google.genai import types
from pydantic import BaseModel

gemini_client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

class ExtractedDataSummary(BaseModel) :
    names : list[str]
    locations : list[str]
    dates : list[str]

input_text = input("Enter the text : \n")
print()
print("----------------------------------------------------------------")

data_extraction_prompt = f"""
Extract all person names, dates, and locations from the text.
Preserve honorifics such as Dr., Professor, Mr., Ms., etc., exactly as they appear in the text.

Text:
{input_text}
"""

extracted_summarized_data = gemini_client.models.generate_content(
     model="gemini-3-flash-preview",
     contents=data_extraction_prompt,
     config=types.GenerateContentConfig(
          response_mime_type="application/json",
          response_schema=ExtractedDataSummary,
     ),
)

extracted_text = extracted_summarized_data.text.strip()
# print(extracted_text)

extracted_data_json = json.loads(extracted_text)

extracted_validated_summary = ExtractedDataSummary.model_validate(extracted_data_json)

print(extracted_validated_summary.model_dump_json(indent=4))