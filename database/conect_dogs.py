from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, Float, Date, TIMESTAMP, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime
# Подключение к базе данных PostgreSQL
DATABASE_URL = 'postgresql+psycopg2://user1:useruser@rc1b-2pdgtp1xwhfy0i47.mdb.yandexcloud.net:6432/mob_dogs?sslmode=verify-full'

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class DatabaseManager:
    def __init__(self, database_url):
        self.engine = create_engine(database_url)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()
        self.Base = declarative_base()

    def add_user(self, db, login, password, email,registration_date, gender=None, phone=None, birthday=None):
        new_user = User(login=login, password=password, email=email, gender=gender, phone=phone, birthday=birthday,registration_date=registration_date)
        db.add(new_user)
        db.commit()
        return new_user.id

    def update_user(self, db, user_id, **kwargs):
        user = db.query(User).filter_by(id=user_id).first()
        if user:
            for key, value in kwargs.items():
                setattr(user, key, value)
            db.commit()
            print(f"Пользователь с ID {user_id} успешно обновлен.")
        else:
            print(f"Пользователь с ID {user_id} не найден.")

    def archive_user(self, db, user_id):
        user = db.query(User).filter_by(id=user_id).first()
        if user:
            user.archived = True
            db.commit()
            print(f"Пользователь с ID {user_id} заархивирован.")
        else:
            print(f"Пользователь с ID {user_id} не найден.")

    def add_dog_collar(self, db, uni_num_dog, name_dog, feeling_hungry, registration_date, deletion_date, health_status):
        new_collar = DogCollar(uni_num_dog=uni_num_dog, name_dog=name_dog, feeling_hungry=feeling_hungry, registration_date=registration_date, deletion_date=deletion_date,health_status=health_status)
        db.add(new_collar)
        db.commit()
        return new_collar.id
  
    def update_dog_collar(self, db, collar_id, **kwargs):
        collar = db.query(DogCollar).filter_by(id=collar_id).first()
        if collar:
            for key, value in kwargs.items():
                setattr(collar, key, value)
            db.commit()
            print(f"Ошейник с ID {collar_id} успешно обновлен.")
        else:
            print(f"Ошейник с ID {collar_id} не найден.")

    def archive_dog_collar(self, db, collar_id):
        collar = db.query(DogCollar).filter_by(id=collar_id).first()
        if collar:
            print(f"Ошейник с ID {collar_id} заархивирован.")
            collar.archived = True
            db.commit()
        else:
            print(f"Ошейник с ID {collar_id} не найден.")


    def add_coordinate(self, db, collar_id, latitude, longitude, timestamp):
        new_coordinate = Coordinate(collar_id=collar_id, latitude=latitude, longitude=longitude, timestamp=timestamp)
        db.add(new_coordinate)
        db.commit()
        return new_coordinate.id

    def query_all_dog_collars(self, db):
        try:
            all_dog_collars = db.query(DogCollar).all()
            return all_dog_collars
        except Exception as e:
            print(f"Ошибка при запросе всех ошейников: {e}")
            return None

    def get_track(self, collar_id: int, start_time: datetime, end_time: datetime):
        try:
            track = self.session.query(Coordinate).filter(
                Coordinate.collar_id == collar_id,
                Coordinate.timestamp >= start_time,
                Coordinate.timestamp <= end_time
            ).all()
            return track
        except Exception as e:
                print(f"An error occurred while retrieving track data: {e}")
                raise e

    def add_task(self, db, id_user_1, id_user_2, id_task, send_date, confirm=False, completion_date=None):
        new_task = Task(id_user_1=id_user_1, id_user_2=id_user_2, id_task=id_task,send_date=send_date, confirm=confirm, completion_date=completion_date)
        db.add(new_task)
        db.commit()
        return new_task.id

    def add_user_dog_collar(self, db, id_user, id_collar,binding_date,unbinding_date=None):
        new_binding = UserDogCollar(id_user=id_user, id_collar=id_collar,binding_date=binding_date, unbinding_date=unbinding_date)
        db.add(new_binding)
        db.commit()
        return new_binding.id_user,new_binding.id_collar

    def update_coordinate(self, db, coordinate_id, **kwargs):
        coordinate = db.query(Coordinate).filter_by(id=coordinate_id).first()
        if coordinate:
            for key, value in kwargs.items():
                setattr(coordinate, key, value)
            db.commit()
            print(f"Координаты с ID {coordinate_id} успешно обновлены.")
        else:
            print(f"Координаты с ID {coordinate_id} не найдены.")

    def delete_coordinate(self, db, coordinate_id):
        coordinate = db.query(Coordinate).filter_by(id=coordinate_id).first()
        if coordinate:
            db.delete(coordinate)
            db.commit()
            print(f"Координаты с ID {coordinate_id} удалены.")
        else:
            print(f"Координаты с ID {coordinate_id} не найдены.")

    def update_task(self, db, task_id, **kwargs):
        task = db.query(Task).filter_by(id=task_id).first()
        if task:
            for key, value in kwargs.items():
                setattr(task, key, value)
            db.commit()
            print(f"Задание с  ID {task_id} успешно обновлено.")
        else:
            print(f"Задание с ID {task_id} не найдено.")

    def archive_task(self, db, task_id):
        task = db.query(Task).filter_by(id=task_id).first()
        if task:
            task.archived = True
            db.commit()
            print(f"Задание с ID {task_id} заархивировано.")
        else:
            print(f"Задание с ID {task_id} не найдено.")

    def update_user_dog_collar(self, db, binding_id, **kwargs):
        binding = db.query(UserDogCollar).filter_by(id=binding_id).first()
        if binding:
            for key, value in kwargs.items():
                setattr(binding, key, value)
            db.commit()
            print(f"Связь пользователя с ошейником с ID {binding_id} успешно обновлена.")
        else:
            print(f"Связь пользователя с ошейником с ID {binding_id} не найдена.")

    def archive_user_dog_collar(self, db, binding_id):
        binding = db.query(UserDogCollar).filter_by(id=binding_id).first()
        if binding:
            binding.archived = True
            db.commit()
            print(f"Связь пользователя с ошейником с ID {binding_id} заархивирована.")
        else:
            print(f"Связь пользователя с ошейником с ID {binding_id} не найдена.")

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    login = Column(String, nullable=False)
    password = Column(String, nullable=False)
    email = Column(String, nullable=False)
    gender = Column(String(10))
    phone = Column(String(20))
    birthday = Column(Date)
    registration_date = Column(TIMESTAMP, default='now()')
    deletion_date = Column(TIMESTAMP, nullable=True)
    archived = Column(Boolean, default=False)

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


rows = result.fetchall()

for row in rows:
    print(row)
