from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

# Схемы для Task
class TaskBase(BaseModel):
    id_user_1: int
    id_user_2: int
    id_task: int
    confirm: bool
    send_date: datetime
    completion_date: Optional[datetime]= None
    task_text : str

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id: int
    archived: bool

    class Config:
        from_attributes = True

class TaskUpdate(BaseModel):
    id_user_1: Optional[int] = None
    id_user_2: Optional[int] = None
    id_task: Optional[int] = None
    confirm: Optional[bool] = None
    send_date: Optional[datetime] = None
    completion_date: Optional[datetime] = None
    archived: Optional[bool] = None
    task_text: Optional[str] =None
