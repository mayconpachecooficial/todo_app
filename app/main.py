from fastapi import FastAPI
from .database import Base, engine
from .routes import tasks

Base.metadata.create_all(bind=engine)

app = FastAPI(title="API de Tarefas")

app.include_router(tasks.router, prefix="/tasks", tags=["Tarefas"])
