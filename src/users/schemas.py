from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class UserBase(BaseModel):
    login: str
    password: str
    email: str
    gender: str
    phone: str
    birthday: datetime
    registration_date: Optional[datetime] = datetime.utcnow()
    deletion_date: Optional[datetime] = None

class UserCreate(UserBase):
    pass

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

class User(UserBase):
    id: int
    archived: bool

    class Config:
        from_attributes = True

