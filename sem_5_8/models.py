from pydantic import BaseModel


class Tasks(BaseModel):
    id: int
    name: str
    description: str
    status: bool = False

