# from fastapi import FastAPI
# from pydantic import BaseModel
# from typing import List

# app = FastAPI()

# class Task(BaseModel):
#     title: str
#     description: str
#     completed: bool

# tasks = []

# # Add a root route
# @app.get("/")
# def read_root():
#     return {"message": "Welcome to the Task Management API!"}

# @app.post("/tasks/", response_model=Task)
# def create_task(task: Task):
#     tasks.append(task)
#     return task

# @app.get("/tasks/", response_model=List[Task])
# def read_tasks():
#     return tasks

# @app.delete("/tasks/{task_id}/")
# def delete_task(task_id: int):
#     if 0 <= task_id < len(tasks):
#         return tasks.pop(task_id)
#     return {"error": "Task not found"}


# FastAPI Implementation
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

app = FastAPI()

class Task(BaseModel):
    id: int
    title: str
    description: str
    completed: bool = False
    created_at: datetime = datetime.now()

class UpdateTask(BaseModel):
    title: Optional[str]
    description: Optional[str]
    completed: Optional[bool]

# In-memory task storage
tasks = []

@app.get("/")
def read_root():
    return {"message": "Welcome to the Task Management API!"}

@app.post("/tasks/", response_model=Task)
def create_task(task: Task):
    if any(t.id == task.id for t in tasks):
        raise HTTPException(status_code=400, detail="Task ID already exists.")
    tasks.append(task)
    return task

@app.get("/tasks/", response_model=List[Task])
def read_tasks(completed: Optional[bool] = None, skip: int = 0, limit: int = 10):
    filtered_tasks = tasks
    if completed is not None:
        filtered_tasks = [task for task in tasks if task.completed == completed]
    return filtered_tasks[skip: skip + limit]

@app.put("/tasks/{task_id}/", response_model=Task)
def update_task(task_id: int, task_data: UpdateTask):
    for index, task in enumerate(tasks):
        if task.id == task_id:
            if task_data.title is not None:
                task.title = task_data.title
            if task_data.description is not None:
                task.description = task_data.description
            if task_data.completed is not None:
                task.completed = task_data.completed
            tasks[index] = task
            return task
    raise HTTPException(status_code=404, detail="Task not found.")

@app.delete("/tasks/{task_id}/")
def delete_task(task_id: int):
    for index, task in enumerate(tasks):
        if task.id == task_id:
            return tasks.pop(index)
    raise HTTPException(status_code=404, detail="Task not found.")
