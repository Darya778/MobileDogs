from fastapi import FastAPI, Depends, HTTPException, APIRouter, Query
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from typing import List, Tuple
from schemas import *
from conect_dogs import User, DogCollar, Coordinate, Task, UserDogCollar, DatabaseManager
from datetime import datetime

# Создаем экземпляр DatabaseManager
db_manager = DatabaseManager('postgresql+psycopg2://user1:useruser@rc1b-2pdgtp1xwhfy0i47.mdb.yandexcloud.net:6432/mob_dogs?sslmode=verify-full')

# Создаем экземпляр FastAPI
app = FastAPI()
router = APIRouter()

# Определяем зависимость для получения сессии базы данных
def get_db():
    db = None
    try:
        db = db_manager.Session()
        yield db
    finally:
        if db:
            db.close()

# Эндпоинты для пользователя (User)
@app.post("/users/", response_model=Tuple[int, str])
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    try:
        user_data=user.dict(exclude={"deletion_date"})
        user_id = db_manager.add_user(db, **user_data)
        return user_id, "Пользователь успешно добавлен."
    except IntegrityError:
        raise HTTPException(status_code=400, detail="User with this login or email already exists")

@app.put("/users/{user_id}", response_model=str)
def update_user(user_id: int, user_update: UserUpdate, db: Session = Depends(get_db)):
    try:
        db_manager.update_user(db, user_id, **user_update.dict(exclude_unset=True))
        return "Пользователь успешно обновлен."
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/users/{user_id}", response_model=str)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    try:
        db_manager.archive_user(db, user_id)
        return "Пользователь успешно удален."
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Эндпоинты для ошейника (DogCollar)
@app.post("/collars/", response_model=Tuple[int,str])
def create_dog_collar(collar: DogCollarCreate, db: Session = Depends(get_db)):
    try:
        collar_id=db_manager.add_dog_collar(db, **collar.dict())
        return collar_id,"Ошейник успешно добавлен."
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.put("/collars/{collar_id}", response_model=str)
def update_dog_collar(collar_id: int, collar_update: DogCollarUpdate, db: Session = Depends(get_db)):
    try:
        db_manager.update_dog_collar(db, collar_id, **collar_update.dict(exclude_unset=True))
        return "Ошейник успешно обновлен."
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/collars/{collar_id}", response_model=str)
def delete_dog_collar(collar_id: int, db: Session = Depends(get_db)):
    try:
        db_manager.archive_dog_collar(db, collar_id)
        return "Ошейник успешно удален."
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/getallcollars/", response_model=List[DogCollarList])
def get_all_dog_collars(db: Session = Depends(get_db)):
    try:
        all_dog_collars = db_manager.query_all_dog_collars(db)
        return list(all_dog_collars)  # Применяем list() для преобразования Cursor в список
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Эндпоинты для координат (Coordinate)
@app.post("/coordinates/", response_model=Tuple[int,str])
def create_coordinate(coordinate: CoordinateCreate, db: Session = Depends(get_db)):
    try:
        coordinate_id=db_manager.add_coordinate(db, **coordinate.dict())
        return coordinate_id,"Координаты успешно добавлены."
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.put("/coordinates/{coordinate_id}", response_model=str)
def update_coordinate(coordinate_id: int, coordinate_update: CoordinateUpdate, db: Session = Depends(get_db)):
    try:
        db_manager.update_coordinate(db, coordinate_id, **coordinate_update.dict(exclude_unset=True))
        return "Координаты успешно обновлены."
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/coordinates/{coordinate_id}", response_model=str)
def delete_coordinate(coordinate_id: int, db: Session = Depends(get_db)):
    try:
        db_manager.delete_coordinate(db, coordinate_id)
        return "Координаты успешно удалены."
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Новый эндпоинт для получения трека
@app.get("/track/", response_model=List[CoordinateBase])
def get_track(
    collar_id: int = Query(..., description="Идентификатор ошейника"),
    start_time: str = Query(..., description="Начальное время периода"),
    end_time: str = Query(..., description="Конечное время периода"),
    db: Session = Depends(get_db)
    ):
    try:
       track = db_manager.get_track(collar_id, start_time, end_time) # Удалите 'db' из параметров
       return track
    except Exception as e:
       raise HTTPException(status_code=500, detail=str(e))

# Эндпоинты для задач (Task)
@app.post("/tasks/", response_model=Tuple[int,str])
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    try:
        task_id=db_manager.add_task(db, **task.dict())
        return task_id,"Задание успешно добавлено."
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.put("/tasks/{task_id}", response_model=str)
def update_task(task_id: int, task_update: TaskUpdate, db: Session = Depends(get_db)):
    try:
        db_manager.update_task(db, task_id, **task_update.dict(exclude_unset=True))
        return "Задание успешно обновлено."
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/tasks/{task_id}", response_model=str)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    try:
        db_manager.archive_task(db, task_id)
        return "Задание успешно удалено."
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Эндпоинты для связи пользователя с ошейником (UserDogCollar)
@app.post("/user-dog-collars/", response_model=Tuple[int,int,str])
def create_user_dog_collar(binding: UserDogCollarCreate, db: Session = Depends(get_db)):
    try:
        userid,dogid= db_manager.add_user_dog_collar(db, **binding.dict())
        return userid,dogid,"Связь пользователя с ошейником успешно добавлена."
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.put("/user-dog-collars/{binding_id}", response_model=str)
def update_user_dog_collar(binding_id: int, binding_update: UserDogCollarUpdate, db: Session = Depends(get_db)):
    try:
        db_manager.update_user_dog_collar(db, binding_id, **binding_update.dict(exclude_unset=True))
        return "Связь пользователя с ошейником успешно обновлена."
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/user-dog-collars/{binding_id}", response_model=str)
def delete_user_dog_collar(binding_id: int, db: Session = Depends(get_db)):
    try:
        db_manager.archive_user_dog_collar(db, binding_id)
        return "Связь пользователя с ошейником успешно удалена."
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
