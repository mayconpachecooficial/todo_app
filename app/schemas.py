from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from .models import StatusEnum

class TaskBase(BaseModel):
    titulo: str
    descricao: str

class TaskCreate(TaskBase):
    pass

class TaskUpdateStatus(BaseModel):
    status: StatusEnum

class TaskOut(TaskBase):
    id: int
    status: StatusEnum
    data_criacao: datetime

    class Config:
        orm_mode = True
