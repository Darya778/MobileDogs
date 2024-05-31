from sqlalchemy import Column, Integer, String, Boolean, Date, TIMESTAMP
from database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    login = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    gender = Column(String(10))
    phone = Column(String(20))
    birthday = Column(Date)
    registration_date = Column(TIMESTAMP, default='now()')
    deletion_date = Column(TIMESTAMP, nullable=True)
    archived = Column(Boolean, default=False)

