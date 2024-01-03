import uvicorn
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sem_5_8.models import Tasks

app = FastAPI()
templates = Jinja2Templates(directory="templates")
tasks = []


# @app.get("/", response_class=HTMLResponse)
# async def read_root(request: Request):
#     return templates.TemplateResponse('index.html', {'request': request})


@app.get("/", response_class=HTMLResponse)
async def get_tasks(request: Request):
    return templates.TemplateResponse('index.html', {'request': request, "tasks": tasks})


@app.get("/tasks/{id_task}")
async def get_task(id_task: int):
    for task in tasks:
        if task.id == id_task:
            return task
    return {"message": "Task not found"}


@app.post("/")
async def add_task(
        request: Request,
        name: str = Form(...),
        description: str = Form(...),
        status: bool = Form(...),
        id: int = Form(...),
):
    task = Tasks(
        id=int(id),
        name=name,
        description=description,
        status=bool(status),
    )
    tasks.append(task)
    return task


@app.put("/tasks/{id_task}")
async def update_task(id_task: int, task: Tasks):
    for task in tasks:
        if task.id == id_task:
            task.name = task.name
            return task
    return {"message": "Task not found"}


@app.delete("/tasks/{id_task}")
async def delete_task(id_task: int):
    for task in tasks:
        if task.id == id_task:
            tasks.remove(task)
            return task
    return {"message": "Task not found"}


if __name__ == '__main__':
    uvicorn.run('sem_5_8.main:app', port=8001, reload=True)
