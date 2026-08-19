from fastapi import FastAPI, BackgroundTasks
from time import sleep
app = FastAPI()

def write_log(message:str):
    sleep(3)
    print(f"{message}")

@app.post("/background")
def llm_reponse(background_task:BackgroundTasks):
    background_task.add_task(write_log,"Log saved : API response sent")
    return "Hello from API"