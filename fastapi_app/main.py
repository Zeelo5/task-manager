from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Task(BaseModel):
    title: str
    description: str
    completed: bool

tasks = []

# Add a root route
@app.get("/")
def read_root():
    return {"message": "Welcome to the Task Management API!"}

@app.post("/tasks/", response_model=Task)
def create_task(task: Task):
    tasks.append(task)
    return task

@app.get("/tasks/", response_model=List[Task])
def read_tasks():
    return tasks

@app.delete("/tasks/{task_id}/")
def delete_task(task_id: int):
    if 0 <= task_id < len(tasks):
        return tasks.pop(task_id)
    return {"error": "Task not found"}
