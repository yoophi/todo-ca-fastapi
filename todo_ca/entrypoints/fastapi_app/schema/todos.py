from pydantic import BaseModel


class TodoOut(BaseModel):
    id: int
    title: str
    completed: bool
