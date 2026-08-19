import asyncio
from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse

app = FastAPI()

async def fast_producer():
    for i in range(5):
        print(f"Producing chunk {i}")

        yield f"data: chunk-{i}\n\n"

        await asyncio.sleep(0.01)


@app.get("/backpressure")
async def backpressure(request: Request):

    async def stream():
        try:
            async for chunk in fast_producer():

                if await request.is_disconnected():
                    print("Client disconnected")
                    break

                print(f"Sending chunk {chunk}")

                yield f"data: chunk-{chunk}\n\n"

                # Simulate a slow consumer
                await asyncio.sleep(1)
                
        except asyncio.CancelledError:

            print("STREAM CANCELLED — CLIENT DISCONNECTED")

            raise

    return StreamingResponse(
        stream(),
        media_type="text/event-stream"
    )