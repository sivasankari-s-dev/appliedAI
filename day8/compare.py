#Comparing sync and async along with streaming
import time
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from provider.async_groq import generate_response as async_generate_response
from provider.groqai_stream import generate_response

app = FastAPI()

def generate_sync_llm():
     start = time.perf_counter()
     sync_response_stream = generate_response("Explain about rain in 5 sentences")
     for chunk in sync_response_stream:

        elapsed = time.perf_counter() - start

        print(
            f"[SYNC] chunk received at {elapsed:.2f}s"
        )

        yield f"data: {chunk}\n\n"

     print(
        f"[SYNC] completed in "
        f"{time.perf_counter() - start:.2f}s"
    )

async def generate_llm():
    start = time.perf_counter()
    response_stream = async_generate_response("Explain about rain in 5 sentences")
    async for chunk in response_stream:
        elapsed = time.perf_counter() - start

        print(
            f"[ASYNC] chunk received at {elapsed:.2f}s"
        )

        yield f"data: {chunk}\n\n"

    print(
        f"[ASYNC] completed in "
        f"{time.perf_counter() - start:.2f}s"
    )

@app.get("/sync-llm")
def sync_llm():
    return StreamingResponse(generate_sync_llm(),media_type="text/event-stream")

@app.get("/async-llm")
async def async_llm():
    return StreamingResponse(generate_llm(),media_type="text/event-stream")