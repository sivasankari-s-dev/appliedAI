from time import sleep
from fastapi import FastAPI
from fastapi.responses import StreamingResponse

app = FastAPI()

# This code defines a generator function called `generate_numbers` that yields numbers from 1 to 5.
# This uses plain text streaming to send the numbers to the client with a 1-second pause between each number.
# There is also a FastAPI endpoint `/stream-numbers` that returns a streaming response using the `generate_numbers` generator function.
# def generate_numbers():
#     for i in range(1, 6):
#         print(f"Generating {i}")
#         sleep(1)  # Sleep for 1 second before yielding the next number
#         yield f"Number: {i}\n"  # Yield the number as a string with a newline character

# @app.get("/stream-numbers")
# def stream_numbers():
#     return StreamingResponse(generate_numbers(), media_type="text/plain")

#SSE 
# This code defines a generator function called `generate_numbers` that yields numbers from 1 to 5 in Server-Sent Events (SSE) format. 
# It uses a for loop to iterate through the range of numbers, and before yielding each number, it sleeps for 1 second. 
# The generator is then used in a FastAPI endpoint `/stream-numbers` that returns a streaming response using the `generate_numbers` generator function with the appropriate media type for SSE.
def generate_numbers():
    for i in range(1, 6):
        print(f"Generating {i}")
        sleep(1)  # Sleep for 1 second before yielding the next number
        yield f"data: Number: {i}\n\n"  # Yield the number as a string with SSE format

@app.get("/stream-numbers")
def stream_numbers():
    return StreamingResponse(generate_numbers(), media_type="text/event-stream")