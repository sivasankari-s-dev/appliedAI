import secrets

from fastapi import  Depends, FastAPI, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials

app = FastAPI()

security = HTTPBasic()

def authenticate(credentials : HTTPBasicCredentials = Depends(security)):
    # Replace these with your actual username and password
    correct_username = "admin"
    correct_password = "password"

    is_correct_username = secrets.compare_digest(credentials.username, correct_username)
    is_correct_password = secrets.compare_digest(credentials.password, correct_password)

    if not (is_correct_username and is_correct_password):
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )

@app.get("/login")
def login(credentials: HTTPBasicCredentials = Depends(security)):
    authenticate(credentials)
    return {"message": "Welcome, " + credentials.username + "!"}