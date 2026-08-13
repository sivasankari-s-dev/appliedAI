import asyncio

from fastapi import FastAPI, HTTPException, Request

from models import ChatResponse

from models import ChatRequest

app = FastAPI()

@app.middleware("http")
async def timing_middleware(request: Request, call_next):
    start_time = asyncio.get_event_loop().time()
    response = await call_next(request)
    process_time = asyncio.get_event_loop().time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    print(f"{request.method} {request.url.path} - {process_time:.2f}s")
    return response

@app.get("/")
async def root():
    return {"message": "Backend is running"}

@app.get("/health")
async def health():
    return {"status": "ok"}

# @app.post("/chat", response_model=ChatResponse)
# async def chat_endpoint(request: ChatRequest):
#     # data = await request.json()
#     # message = data.get("message", "")
#     # Simulate processing the message
#     await asyncio.sleep(2)  # Simulate some processing delay
#     response_text = f"Processed message: {request.message}"
#     return ChatResponse(response=response_text)

@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    try:
        raise Exception("Something wrong with AI model")
    except Exception:
        raise HTTPException(
            status_code=500, detail="AI service is currently unavailable. Please try again later."
        )