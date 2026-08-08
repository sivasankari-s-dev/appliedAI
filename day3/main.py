import json

from prompts import entity_extraction_prompt
from providers.gemini import GeminiProvider
from providers.claude import ClaudeProvider
from schemas import ExtractedDataSummary


provider = GeminiProvider()
# provider = ClaudeProvider()

input_text = input("Enter the text:\n")

prompt = f"""
{entity_extraction_prompt}

Text:
{input_text}
"""

response_text = provider.generate(prompt)

response_data = json.loads(response_text)

extracted_entities = ExtractedDataSummary.model_validate(response_data)

print(extracted_entities.model_dump_json(indent=4))