from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, Float, Date, TIMESTAMP, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship

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
     def add_record(self, model, **kwargs):
        new_record = model(**kwargs)
        self.session.add(new_record)
        self.session.commit()
        print(f"Запись успешно добавлена в таблицу {model.__tablename__}.")

    def update_record(self, model, record_id, **kwargs):
        record = self.session.query(model).filter_by(id=record_id).first()
        
        if record:
            for key, value in kwargs.items():
                setattr(record, key, value)
            self.session.commit()
            print(f"Запись с ID {record_id} успешно обновлена в таблице {model.__tablename__}.")
        else:
            print(f"Запись с ID {record_id} не найдена в таблице {model.__tablename__}.")
            
    def delete_record(self, model, record_id):
        record = self.session.query(model).filter_by(id=record_id).first()
        
        if record:
            self.session.delete(record)
            self.session.commit()
            print(f"Запись с ID {record_id} удалена из таблицы {model.__tablename__}.")
        else:
            print(f"Запись с ID {record_id} не найдена в таблице {model.__tablename__}.")
            
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

class DogCollar(Base):
    __tablename__ = 'dogs_collar'

    id = Column(Integer, primary_key=True)
    uni_num_dog = Column(String, nullable=False)
    name_dog = Column(String, nullable=False)
    temp = Column(Float)
    feeling_hungry = Column(Boolean)
    health_status = Column(String)
    registration_date = Column(TIMESTAMP, default='now()')
    deletion_date = Column(TIMESTAMP, nullable=True)
class UserDogCollar(Base):
    __tablename__ = 'users_dogs_collar'

    id = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey('users.id'), nullable=False)
    id_collar = Column(Integer, ForeignKey('dogs_collar.id'), nullable=False)
    binding_date = Column(TIMESTAMP, default='now()')
    unbinding_date = Column(TIMESTAMP, nullable=True)

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    id_user_1 = Column(Integer, ForeignKey('users.id'), nullable=False)
    id_user_2 = Column(Integer, ForeignKey('users.id'), nullable=False)
    id_task = Column(Integer, nullable=False)
    confirm = Column(Boolean, default=False)
    send_date = Column(TIMESTAMP, default='now()')
    completion_date = Column(TIMESTAMP, nullable=True)
result = engine.execute("SELECT * From users")

rows = result.fetchall()

for row in rows:
    print(row)
