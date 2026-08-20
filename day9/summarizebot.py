import uuid, json
from fastapi import FastAPI, BackgroundTasks
from provider.groqai import generate_response

app = FastAPI()

def get_id():
    return uuid.uuid4().hex

def bg_summary(summary_id, prompt):
    # id = get_id()
    response = generate_response(prompt)
    summary = {
              "id":summary_id,
              "summary":response
    }
    with open ("summary.json1", "a") as file:
        file.write(json.dumps(summary) + "\n")

@app.post("/summarize")
def summarize_document(background_task:BackgroundTasks,request:str):
    # text =input("Enter the text to summarize: ")
    prompt = f"summarize the text into 3 bullet executive briefing {request}"
    summary_id = get_id()
    background_task.add_task(bg_summary,summary_id,prompt)
    # response = generate_response(prompt)
    return {
        "id":summary_id,
        "Status": " Processing"
    }

@app.get("/summary/{id}")
def get_summary(id:str):
    specific_record = None
    with open ("summary.json1", "r") as file:
        for line in file:
            # Clean up any accidental blank lines
            if not line.strip():
                continue
                
            record = json.loads(line)
            
            # 3. If a match is found, return it immediately
            if record.get("id") == id:
                specific_record =record
                break
        if specific_record:
            return specific_record
        else:
            return "No summary found"
