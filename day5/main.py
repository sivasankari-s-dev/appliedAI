from fastapi import FastAPI
from models import ChatRequest, ChatResponse, SummarizeRequest, SummarizeResponse
from service.groqai import generate_response

app = FastAPI()

@app.get("/")
def root():
    return {"message": "AI Backend is running"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/chat", response_model=ChatResponse)
def chat_endpoint(request: ChatRequest):
    response_text = generate_response(request.message)
    return ChatResponse(response=response_text)


@app.post("/summarize", response_model=SummarizeResponse)
def summarize_endpoint(response: SummarizeRequest):
    summary_text = generate_response(f"Summarize the following text: {response.text}")
    return SummarizeResponse(summary=summary_text)