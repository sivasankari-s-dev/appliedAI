# import asyncio
from fastapi import FastAPI
from time import sleep
from fastapi.responses import StreamingResponse
from provider.async_groq import generate_response

app = FastAPI()

async def generate_llm():
    response_stream = generate_response("Explain about rain in 5 sentences")
    async for chunk in response_stream:
    #    sleep(1)  # Sleep for 1 second before yielding the next response
       yield f"data: {chunk}\n\n"

@app.get("/stream-llm")
async def stream_llm():
    return StreamingResponse(generate_llm(),media_type="text/event-stream")