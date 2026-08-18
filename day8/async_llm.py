import asyncio
from fastapi import FastAPI, Request
from time import sleep
from fastapi.responses import StreamingResponse
from provider.async_groq import generate_response

app = FastAPI()

async def generate_llm():
    response_stream = generate_response("Explain about rain in 5 sentences")
    async for chunk in response_stream:
    #    sleep(1)  # Sleep for 1 second before yielding the next response
       yield f"data: {chunk}\n\n"

@app.middleware("http")
async def timing_middleware(request: Request, call_next):
    start_time = asyncio.get_event_loop().time()
    response = await call_next(request)
    process_time = asyncio.get_event_loop().time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    print(f"{request.method} {request.url.path} - {process_time:.2f}s")
    return response

@app.get("/stream-llm")
async def stream_llm():
    return StreamingResponse(generate_llm(),media_type="text/event-stream")