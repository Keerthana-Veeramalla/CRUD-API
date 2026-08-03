from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import Optional

app = FastAPI(
    title="Task API",
    description="A simple CRUD API built with FastAPI",
    version="1.0"
)


# -----------------------------
# Request Model
# -----------------------------
class TaskCreate(BaseModel):
    title: str


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    done: Optional[bool] = None


# -----------------------------
# In-memory Database
# -----------------------------
tasks = [
    {
        "id": 1,
        "title": "Study FastAPI",
        "done": False
    },
    {
        "id": 2,
        "title": "Buy Milk",
        "done": True
    },
    {
        "id": 3,
        "title": "Complete Assignment",
        "done": False
    }
]


# -----------------------------
# Home Endpoint
# -----------------------------
@app.get("/")
def home():
    return {
        "name": "Task API",
        "version": "1.0",
        "endpoints": [
            "/tasks"
        ]
    }


# -----------------------------
# Health Check
# -----------------------------
@app.get("/health")
def health():
    return {
        "status": "ok"
    }


# -----------------------------
# Get All Tasks
# -----------------------------
@app.get("/tasks")
def get_tasks():
    return tasks


# -----------------------------
# Get Single Task
# -----------------------------
@app.get("/tasks/{task_id}")
def get_task(task_id: int):

    for task in tasks:
        if task["id"] == task_id:
            return task

    raise HTTPException(
        status_code=404,
        detail=f"Task {task_id} not found"
    )


# -----------------------------
# Create Task
# -----------------------------
@app.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate):

    if task.title.strip() == "":
        raise HTTPException(
            status_code=400,
            detail="Title cannot be empty"
        )

    new_id = max([t["id"] for t in tasks], default=0) + 1

    new_task = {
        "id": new_id,
        "title": task.title,
        "done": False
    }

    tasks.append(new_task)

    return new_task


# -----------------------------
# Update Task
# -----------------------------
@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: TaskUpdate):

    for task in tasks:

        if task["id"] == task_id:

            if updated_task.title is not None:

                if updated_task.title.strip() == "":
                    raise HTTPException(
                        status_code=400,
                        detail="Title cannot be empty"
                    )

                task["title"] = updated_task.title

            if updated_task.done is not None:
                task["done"] = updated_task.done

            return task

    raise HTTPException(
        status_code=404,
        detail=f"Task {task_id} not found"
    )


# -----------------------------
# Delete Task
# -----------------------------
@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int):

    for task in tasks:

        if task["id"] == task_id:
            tasks.remove(task)
            return

    raise HTTPException(
        status_code=404,
        detail=f"Task {task_id} not found"
    )