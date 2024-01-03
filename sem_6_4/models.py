from pydantic import BaseModel, Field


class Task(BaseModel):
    id: int
    title: str = Field(..., max_length=30, title='Title')
    description: str = Field(max_length=128, title='Description')
    status: bool = Field(..., title='Status')


class TaskIn(BaseModel):
    title: str = Field(..., max_length=30, title='Title')
    description: str = Field(max_length=128, title='Description')
    status: bool = Field(..., title='Status')