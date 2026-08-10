import json

from prompts import entity_extraction_prompt
# from providers.gemini import GeminiProvider
# from providers.claude import ClaudeProvider
from providers.groqai import GroqProvider
from schemas import ExtractedDataSummary


# provider = GeminiProvider()
# provider = ClaudeProvider()
provider = GroqProvider()

input_text = input("Enter the text:\n")

prompt = f"""
{entity_extraction_prompt}

Text:
{input_text}
"""

response_text = provider.generate(prompt)

# print(response_text)

response_data = json.loads(response_text)

extracted_entities = ExtractedDataSummary.model_validate(response_data)

print(extracted_entities.model_dump_json(indent=4))