from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Tuple
from datetime import datetime
from database import get_db
from database_manager import  DatabaseManager
from .schemas import *
from sqlalchemy.exc import IntegrityError
from users.hash_psw import get_password_hash

router = APIRouter()
db_manager=DatabaseManager('postgresql+psycopg2://user1:useruser@rc1b-2pdgtp1xwhfy0i47.mdb.yandexcloud.net:6432/mob_dogs?sslmode=verify-full')

@router.post("/users", response_model=Tuple[int, str])
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    try:
        hashed_password = get_password_hash(user.password)
        user_data = user.dict(exclude={"deletion_date"})
        user_data["password"] = hashed_password
        user_id, user_answer = db_manager.add_user(db, **user_data)
        if user_id==0:
            raise HTTPException(status_code=500,detail=user_answer)
        return user_id, user_answer
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)+str(user_answer))

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


