from fastapi import FastAPI
import uvicorn
from typing import Optional
from pydantic import BaseModel
import secrets

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

from starlette_exporter import PrometheusMiddleware, handle_metrics

app = FastAPI()

security = HTTPBasic()

def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(credentials.username, "test")
    correct_password = secrets.compare_digest(credentials.password, "test")
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username

app.add_middleware(PrometheusMiddleware)
app.add_route("/metrics", handle_metrics)

@app.get("/")
def read_root(credentials: HTTPBasicCredentials = Depends(get_current_username)):
    return {"Hello from OTUS!!)"}

@app.get("/check")
def hello():
    return "Hello World"


#uvicorn.run(app, host="127.0.0.1", port="8080")