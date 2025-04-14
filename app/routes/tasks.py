from fastapi import APIRouter, Depends, HTTPException, Header
from sqlalchemy.orm import Session
from typing import List, Optional
from .. import crud, schemas, database

router = APIRouter()

FAKE_TOKEN = "123456"

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

def verify_token(x_token: str = Header(...)):
    if x_token != FAKE_TOKEN:
        raise HTTPException(status_code=401, detail="Token inválido")

@router.post("/", response_model=schemas.TaskOut, dependencies=[Depends(verify_token)])
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    return crud.create_task(db, task)

@router.get("/", response_model=List[schemas.TaskOut], dependencies=[Depends(verify_token)])
def list_tasks(status: Optional[str] = None, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_tasks(db, status, skip, limit)

@router.patch("/{task_id}", response_model=schemas.TaskOut, dependencies=[Depends(verify_token)])
def update_status(task_id: int, update: schemas.TaskUpdateStatus, db: Session = Depends(get_db)):
    task = crud.update_task_status(db, task_id, update.status)
    if not task:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return task

@router.delete("/{task_id}", dependencies=[Depends(verify_token)])
def delete_task(task_id: int, db: Session = Depends(get_db)):
    success = crud.delete_task(db, task_id)
    if not success:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return {"message": "Tarefa removida com sucesso"}
