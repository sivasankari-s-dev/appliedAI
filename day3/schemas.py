from pydantic import BaseModel

class ExtractedDataSummary(BaseModel) :
    names: list[str]
    locations: list[str]
    dates: list[str]