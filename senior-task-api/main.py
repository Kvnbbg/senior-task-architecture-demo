from fastapi import FastAPI, HTTPException, Query
from typing import List, Optional
from models import Task, TaskCreate, TaskUpdate, TaskStatus
from service import TaskService

app = FastAPI(
    title="Senior Task API",
    description="Strictly typed, isolated task management service. Anti-vibe-coding architecture.",
    version="1.0.0",
)

service = TaskService()


@app.post("/tasks", response_model=Task, status_code=201)
def create_task(data: TaskCreate) -> Task:
    return service.create(data)


@app.get("/tasks", response_model=List[Task])
def list_tasks(status: Optional[TaskStatus] = Query(None)) -> List[Task]:
    return service.list(status=status)


@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int) -> Task:
    task = service.get(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@app.patch("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, data: TaskUpdate) -> Task:
    task = service.update(task_id, data)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int) -> None:
    if not service.delete(task_id):
        raise HTTPException(status_code=404, detail="Task not found")
