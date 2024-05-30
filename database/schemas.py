from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

# Схемы для DogCollar
class DogCollarBase(BaseModel):
    uni_num_dog: int
    name_dog: str
    feeling_hungry: bool
    registration_date: datetime
    deletion_date: Optional[datetime]= None
    health_status: str

class DogCollarCreate(DogCollarBase):
    pass

class DogCollar(DogCollarBase):
    id: int
    archived: bool

    class Config:
        from_attributes = True

class DogCollarUpdate(BaseModel):
    uni_num_dog: Optional[int] = None
    name_dog: Optional[str] = None
    feeling_hungry: Optional[bool] = None
    registration_date: Optional[datetime] = None
    deletion_date: Optional[datetime] = None
    health_status: Optional[str] = None
    archived: Optional[bool] = None

class DogCollarList(BaseModel):
    uni_num_dog: int
    name_dog: str
    feeling_hungry: bool
    registration_date:datetime
    deletion_date: Optional[datetime]= None
    health_status: str

# Схемы для Coordinate
class CoordinateBase(BaseModel):
    collar_id: int
    latitude: float
    longitude: float
    timestamp: str

class CoordinateCreate(CoordinateBase):
    pass

class Coordinate(CoordinateBase):
    id: int

    class Config:
        from_attributes = True

class CoordinateUpdate(BaseModel):
    collar_id: Optional[int] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    timestamp: Optional[str] = None

# Схемы для User
class UserBase(BaseModel):
    login: str
    password: str
    email: str
    gender: str
    phone: str
    birthday: datetime
    registration_date: Optional[datetime] = Field(default_factory=datetime.utcnow)
    deletion_date: Optional[datetime]= None

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    archived: bool

    class Config:
        from_attributes = True

class UserUpdate(BaseModel):
    login: Optional[str] = None
    password: Optional[str] = None
    email: Optional[str] = None
    gender: Optional[str] = None
    phone: Optional[str] = None
    birthday: Optional[datetime] = None
    registration_date: Optional[datetime] = None
    deletion_date: Optional[datetime] = None
    archived: Optional[bool] = None

# Схемы для Task
class TaskBase(BaseModel):
    id_user_1: int
    id_user_2: int
    id_task: int
    confirm: bool
    send_date: datetime
    completion_date: Optional[datetime]= None

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id: int
    archived: bool

    class Config:
        from_attributes = True

class TaskUpdate(BaseModel):
    id_user_1: Optional[int] = None
    id_user_2: Optional[int] = None
    id_task: Optional[int] = None
    confirm: Optional[bool] = None
    send_date: Optional[datetime] = None
    completion_date: Optional[datetime] = None
    archived: Optional[bool] = None

# Схемы для UserDogCollar
class UserDogCollarBase(BaseModel):
    id_user: int
    id_collar: int
    binding_date: datetime
    unbinding_date: Optional[datetime]=None

class UserDogCollarCreate(UserDogCollarBase):
    pass

class UserDogCollar(UserDogCollarBase):
    id: int
    archived: bool

    class Config:
        from_attributes = True

class UserDogCollarUpdate(BaseModel):
    id_user: Optional[int] = None
    id_collar: Optional[int] = None
    binding_date: Optional[datetime] = None
    unbinding_date: Optional[datetime] = None
    archived: Optional[bool] = None

# Схема для TrackQuery
class TrackQuery(BaseModel):
    collar_id: int
    start_time: datetime
    end_time: datetime
