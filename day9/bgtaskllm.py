from fastapi import FastAPI, BackgroundTasks
from time import sleep
from datetime import datetime
from provider.groqai import generate_response

app = FastAPI()

def write_log(prompt:str,response:str):
    with open ("chat_logs.txt","a",encoding="utf-8") as file:
        file.write(f"\n-----{datetime.now()}------\n")
        file.write(f"Prompt : {prompt}\n")
        file.write(f"Response: {response}\n")

@app.post("/chat")
def llm_chat(background_task:BackgroundTasks):
    prompt = "What is multi threading?"
    response = generate_response(prompt)
    background_task.add_task(write_log,prompt,response)
    return response