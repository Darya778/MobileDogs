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
     def add_user(self, login, password, email, gender=None, phone=None, birthday=None):

        # Создаем нового пользователя
        new_user = User(login=login, password=password, email=email, gender=gender, phone=phone, birthday=birthday)

        # Добавляем пользователя в сессию
        self.session.add(new_user)
        # Фиксируем изменения в базе данных
        self.session.commit()
        print("Пользователь успешно добавлен.")

    def update_user(self, user_id, **kwargs):

        # Находим пользователя по user_id
        user = self.session.query(User).filter_by(id=user_id).first()

        if user:
            # Обновляем атрибуты пользователя на основе переданных параметров
            for key, value in kwargs.items():
                setattr(user, key, value)
            # Фиксируем изменения в базе данных
            self.session.commit()
            print(f"Пользователь с ID {user_id} успешно обновлен.")
        else:
            print(f"Пользователь с ID {user_id} не найден.")
    def delete_user(self, user_id):
        # Находим пользователя по user_id
        user = self.session.query(User).filter_by(id=user_id).first()
        if user:
            # Удаляем пользователя из сессии
            self.session.delete(user)
            # Фиксируем изменения в базе данных
            self.session.commit()
            print(f"Пользователь с ID {user_id} удалён.")
        else:
            print(f"Пользователь с ID {user_id} не найден.")


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
