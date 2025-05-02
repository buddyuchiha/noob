from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional 

app = FastAPI()

class Task(BaseModel):
    name: str 
    description: Optional[str] = None 

@app.get("/home")
def get_tasks():
    return {"data" : "дом"}

@app.get("/tasks")
def get_tasks():
    task = Task(name="Запиши это видео")
    return {"data" : task}

