import sys
sys.path.insert(1, '../log')
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Tuple
from database import get_db
from database_manager import DatabaseManager
from .schemas import *
from sqlalchemy.exc import IntegrityError
from log_tasks import log_message

router = APIRouter()
db_manager=DatabaseManager('postgresql+psycopg2://user1:useruser@rc1b-2pdgtp1xwhfy0i47.mdb.yandexcloud.net:6432/mob_dogs?sslmode=verify-full')


@router.post("/tasks", response_model=Tuple[int,str,str])
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    try:
        task_id,task_text=db_manager.add_task(db, **task.dict())
        log_message("info", "200 OK - Задание успешно добавлено.")
        return task_id,"Задание успешно добавлено.",task_text
    except Exception as e:
        log_message("error", "500 "+str(e))
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/tasks/{task_id}", response_model=str)
def update_task(task_id: int, task_update: TaskUpdate, db: Session = Depends(get_db)):
    try:
        db_manager.update_task(db, task_id, **task_update.dict(exclude_unset=True))
        log_message("info", "200 OK - Задание успешно обновлено.")
        return "Задание успешно обновлено."
    except Exception as e:
        log_message("error", "500 "+str(e))
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/tasks/{task_id}", response_model=str)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    try:
        db_manager.archive_task(db, task_id)
        log_message("info", "200 OK - Задание успешно удалено.")
        return "Задание успешно удалено."
    except Exception as e:
        log_message("error", "500 "+str(e))
        raise HTTPException(status_code=500, detail=str(e))
