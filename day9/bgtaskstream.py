from fastapi import FastAPI, BackgroundTasks
from fastapi.responses import StreamingResponse
from datetime import datetime
from provider.groqstreamai import generate_response

app = FastAPI()

def write_log(prompt:str,response:str):
    with open ("chat_logs.txt","a",encoding="utf-8") as file:
        file.write(f"\n-----{datetime.now()}------\n")
        file.write(f"Prompt : {prompt}\n")
        file.write(f"Response: {response}\n")

def generate_llm_response(background_task:BackgroundTasks):
    prompt = "What is multi threading?"
    full_response = ""
    response = generate_response(prompt)
    for chunk in response:
        full_response += chunk
        yield f"data:{chunk} \n\n"
    background_task.add_task(write_log,prompt,full_response)

@app.post("/chat")
def llm_chat(background_task:BackgroundTasks):
    return StreamingResponse(generate_llm_response(background_task),media_type="text/event-stream")