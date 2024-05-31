import sys
sys.path.insert(1, '../log')
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Tuple
from database import get_db
from database_manager import DatabaseManager
from devices.schemas import *
from log_devices import log_message

router = APIRouter()
db_manager=DatabaseManager('postgresql+psycopg2://user1:useruser@rc1b-2pdgtp1xwhfy0i47.mdb.yandexcloud.net:6432/mob_dogs?sslmode=verify-full')

# DogCollar Endpoints
@router.post("/collars", response_model=Tuple[int, str])
def create_dog_collar(collar: DogCollarCreate, db: Session = Depends(get_db)):
    try:
        collar_id = db_manager.add_dog_collar(db, **collar.dict())
        log_message("info", "200 Ok - Ошейник успешно добавлен.")
        return collar_id, "Ошейник успешно добавлен."
    except Exception as e:
        log_message("error", "500 "+str(e))
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/collars/{collar_id}", response_model=str)
def update_dog_collar(collar_id: int, collar_update: DogCollarUpdate, db: Session = Depends(get_db)):
    try:
        db_manager.update_dog_collar(db, collar_id, **collar_update.dict(exclude_unset=True))
        log_message("info", "200 Ok - Ошейник успешно обновлен.")
        return "Ошейник успешно обновлен."
    except Exception as e:
        log_message("error", "500 "+str(e))
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/collars/{collar_id}", response_model=str)
def delete_dog_collar(collar_id: int, db: Session = Depends(get_db)):
    try:
        db_manager.archive_dog_collar(db, collar_id)
        log_message("info", "200 OK - Ошейник успешно удален.")
        return "Ошейник успешно удален."
    except Exception as e:
        log_message("error", "500 "+str(e))
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/getallcollars/", response_model=List[DogCollarList])
def get_all_dog_collars(db: Session = Depends(get_db)):
    try:
        all_dog_collars = db_manager.query_all_dog_collars(db)
        log_message("info", "200 OK - Список всех ошейников получен.")
        return list(all_dog_collars)
    except Exception as e:
        log_message("error", "500 "+str(e))
        raise HTTPException(status_code=500, detail=str(e))

# Coordinate Endpoints
@router.post("/coordinates", response_model=Tuple[int, str])
def create_coordinate(coordinate: CoordinateCreate, db: Session = Depends(get_db)):
    try:
        coordinate_id = db_manager.add_coordinate(db, **coordinate.dict())
        log_message("info", "200 Ok - Координаты успешно добавлены.")
        return coordinate_id, "Координаты успешно добавлены."
    except Exception as e:
        log_message("error", "500 "+str(e))
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/coordinates/{coordinate_id}", response_model=str)
def update_coordinate(coordinate_id: int, coordinate_update: CoordinateUpdate, db: Session = Depends(get_db)):
    try:
        db_manager.update_coordinate(db, coordinate_id, **coordinate_update.dict(exclude_unset=True))
        log_message("info", "200 OK - Координаты успешно обновлены.")
        return "Координаты успешно обновлены."
    except Exception as e:
        log_message("error", "500 "+str(e))
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/coordinates/{coordinate_id}", response_model=str)
def delete_coordinate(coordinate_id: int, db: Session = Depends(get_db)):
    try:
        db_manager.delete_coordinate(db, coordinate_id)
        log_message("info", "200 OK - Координаты успешно удалены.")
        return "Координаты успешно удалены."
    except Exception as e:
        log_message("error", "500 "+str(e))
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/track", response_model=List[CoordinateBase])
def get_track(
    collar_id: int = Query(..., description="Идентификатор ошейника"),
    start_time: str = Query(..., description="Начальное время периода"),
    end_time: str = Query(..., description="Конечное время периода"),
    db: Session = Depends(get_db)
):
    try:
        track = db_manager.get_track(collar_id, start_time, end_time)
        log_message("info", "200 OK")
        return track
    except Exception as e:
        log_message("error", "500 "+str(e))
        raise HTTPException(status_code=500, detail=str(e))

# Эндпоинты для связи пользователя с ошейником (UserDogCollar)
@router.post("/user-dog-collars", response_model=Tuple[int,int,str])
def create_user_dog_collar(binding: UserDogCollarCreate, db: Session = Depends(get_db)):
    try:
        userid,dogid= db_manager.add_user_dog_collar(db, **binding.dict())
        log_message("info", "200 OK - Связь пользователя с ошейником успешно добавлена.")
        return userid,dogid,"Связь пользователя с ошейником успешно добавлена."
    except Exception as e:
        log_message("error", "500 "+str(e))
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/user-dog-collars/{binding_id}", response_model=str)
def update_user_dog_collar(binding_id: int, binding_update: UserDogCollarUpdate, db: Session = Depends(get_db)):
    try:
        db_manager.update_user_dog_collar(db, binding_id, **binding_update.dict(exclude_unset=True))
        log_message("info", "200 OK - Связь пользователя с ошейником успешно обновлена.")
        return "Связь пользователя с ошейником успешно обновлена."
    except Exception as e:
        log_message("error", "500 "+str(e))
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/user-dog-collars/{binding_id}", response_model=str)
def delete_user_dog_collar(binding_id: int, db: Session = Depends(get_db)):
    try:
        db_manager.archive_user_dog_collar(db, binding_id)
        log_message("info", "200 OK - Связь пользователя с ошейником успешно удалена.")
        return "Связь пользователя с ошейником успешно удалена."
    except Exception as e:
        log_message("error", "500 "+str(e))
        raise HTTPException(status_code=500, detail=str(e))
