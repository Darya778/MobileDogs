from sqlalchemy import Column, Integer, String, Boolean, Date, TIMESTAMP, Float, ForeignKey
from database import Base


class DogCollar(Base):
    __tablename__ = 'dogs_collar'

    id = Column(Integer, primary_key=True)
    uni_num_dog = Column(String, nullable=False)
    name_dog = Column(String, nullable=False)
    feeling_hungry = Column(Boolean)
    health_status = Column(String)
    registration_date = Column(TIMESTAMP, default='now()')
    deletion_date = Column(TIMESTAMP, nullable=True)
    archived = Column(Boolean, default=False)

class UserDogCollar(Base):
    __tablename__ = 'users_dogs_collar'

    id = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey('users.id'), nullable=False)
    id_collar = Column(Integer, ForeignKey('dogs_collar.id'), nullable=False)
    binding_date = Column(TIMESTAMP, default='now()')
    unbinding_date = Column(TIMESTAMP, default=None)
    archived = Column(Boolean, default=False)

class Coordinate(Base):
    __tablename__ = 'coordinates'
    id = Column(Integer, primary_key=True)
    collar_id = Column(Integer, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    timestamp = Column(TIMESTAMP, default='now()')

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    id_user_1 = Column(Integer, ForeignKey('users.id'), nullable=False)
    id_user_2 = Column(Integer, ForeignKey('users.id'), nullable=False)
    id_task = Column(Integer, nullable=False)
    confirm = Column(Boolean, default=False)
    send_date = Column(TIMESTAMP, default='now()')
    completion_date = Column(TIMESTAMP, nullable=True)
    archived = Column(Boolean, default=False)
