from time import sleep
from fastapi import FastAPI
from fastapi.responses import StreamingResponse

app = FastAPI()

def fake_llm():
    responses = [
        "Hello",
        "How are you?",
        "I am a fake LLM.",
        "I can generate text.",
        "This is a streaming response.",
        "Goodbye!"
    ]
    for response in responses:
        print(f"Generating response: {response}")
        sleep(1)  # Sleep for 1 second before yielding the next response
        yield f"data: {response}\n\n"  # Yield the response as a string with SSE format

@app.get("/stream-llm")
def stream_llm():
    return StreamingResponse(fake_llm(), media_type="text/event-stream")
