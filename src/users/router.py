from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Tuple
from datetime import datetime
from ..database import get_db
from ..database import db_manager
from .schemas import *
from sqlalchemy.exc import IntegrityError

router = APIRouter()

@router.post("/users/", response_model=Tuple[int, str])
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    try:
        user_data = user.dict(exclude={"deletion_date"})
        user_id = db_manager.add_user(db, **user_data)
        return user_id, "Пользователь успешно добавлен."
    except IntegrityError:
        raise HTTPException(status_code=400, detail="User with this login or email already exists")

@router.put("/users/{user_id}", response_model=str)
def update_user(user_id: int, user_update: UserUpdate, db: Session = Depends(get_db)):
    try:
        db_manager.update_user(db, user_id, **user_update.dict(exclude_unset=True))
        return "Пользователь успешно обновлен."
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/users/{user_id}", response_model=str)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    try:
        db_manager.archive_user(db, user_id)
        return "Пользователь успешно удален."
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

