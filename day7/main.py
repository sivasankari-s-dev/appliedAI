# Error handling and logging in FastAPI application
import logging
from fastapi import FastAPI, HTTPException
from models import ChatRequest, ChatResponse
from provider.groqai import generate_response

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    try:
        #    # Deliberately create an error
        # result = 10 / 0

        # return ChatResponse(message=str(result))
        response_message = generate_response(request.message)
        return ChatResponse(message=response_message)
    except Exception as e:
          print("========== ACTUAL ERROR ==========")
          print(type(e).__name__)
          print(str(e))
          print("===================================")
          logger.exception("AI Service Failed: %s", e)
          raise HTTPException(status_code=500, detail="AI Service is unavailable")