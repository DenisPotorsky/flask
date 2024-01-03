from fastapi import FastAPI
from models import Task, TaskIn
import sqlalchemy
import databases
from typing import List

# Задание 4

app = FastAPI()
DATABASE_URL = "sqlite:///tasks.db"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()
tasks = sqlalchemy.Table("tasks", metadata,
                         sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
                         sqlalchemy.Column("title", sqlalchemy.String(30)),
                         sqlalchemy.Column("description", sqlalchemy.String(128)),
                         sqlalchemy.Column('status', sqlalchemy.Boolean))

engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
metadata.create_all(engine)


@app.get('/tasks/', response_model=List[Task])
async def get_all_tasks():
    query = tasks.select()
    return await database.fetch_all(query)


@app.get('/tasks/{task_id}/', response_model=Task)
async def get_one_task(task_id: int):
    query = tasks.select().where(tasks.c.id == task_id)
    return await database.fetch_one(query)


@app.post('/tasks/', response_model=Task)
async def create_task(task: TaskIn):
    query = tasks.insert().values(title=task.title, description=task.description, status=task.status)
    last_record_id = await database.execute(query)
    return {**task.dict(), 'id': last_record_id}


@app.put('/tasks/{task_id}/', response_model=Task)
async def update_task(task_id: int, new_user=TaskIn):
    query = tasks.update().where(tasks.c.id == task_id).values(**new_user.dict())
    await database.execute(query)
    return {**new_user.dict(), 'id': new_user}


@app.delete('/tasks/{task_id}/')
async def delete_task(task_id: int):
    query = tasks.delete().where(tasks.c.id == task_id)
    await database.execute(query)
    return {'message': 'Task deleted'}
