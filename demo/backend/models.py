from pydantic import BaseModel

class TodoBase(BaseModel):
    title: str
    completed: bool = False

class TodoCreate(TodoBase):
    pass

class TodoUpdate(BaseModel):
    title: str | None = None
    completed: bool | None = None

class TodoResponse(TodoBase):
    id: int
    time_spent: int = 0
    is_running: bool = False

    class Config:
        from_attributes = True
