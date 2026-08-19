import time
from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse

app=FastAPI()

def fake_llm():

    for i in range(20):

        time.sleep(1)

        yield f"chunk-{i}"

@app.get("/test-stream")
async def test_stream(request: Request):

    async def stream():

        for chunk in fake_llm():

            if await request.is_disconnected():

                print("CLIENT DISCONNECTED")

                break

            yield f"data: {chunk}\n\n"

    return StreamingResponse(
        stream(),
        media_type="text/event-stream"
    )