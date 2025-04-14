from sqlalchemy.orm import Session
from . import models, schemas
from typing import List, Optional

def get_tasks(db: Session, status: Optional[str] = None, skip: int = 0, limit: int = 10) -> List[models.Task]:
    query = db.query(models.Task)
    if status:
        query = query.filter(models.Task.status == status)
    return query.offset(skip).limit(limit).all()

def create_task(db: Session, task: schemas.TaskCreate) -> models.Task:
    db_task = models.Task(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def update_task_status(db: Session, task_id: int, status: str) -> Optional[models.Task]:
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if task:
        task.status = status
        db.commit()
        db.refresh(task)
    return task

def delete_task(db: Session, task_id: int) -> bool:
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if task:
        db.delete(task)
        db.commit()
        return True
    return False
