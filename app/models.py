from sqlalchemy import Column, Integer, String, DateTime, Enum
from datetime import datetime
import enum
from .database import Base

class StatusEnum(str, enum.Enum):
    pendente = "pendente"
    concluida = "concluida"

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, index=True)
    descricao = Column(String)
    status = Column(Enum(StatusEnum), default=StatusEnum.pendente)
    data_criacao = Column(DateTime, default=datetime.utcnow)
    