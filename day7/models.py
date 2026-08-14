from pydantic import BaseModel,Field

class ChatResponse(BaseModel):
    message: str 

class ChatRequest(BaseModel):
    message: str= Field(min_length=1)