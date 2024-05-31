from sqlalchemy import Column, Integer, String, Boolean, Date, TIMESTAMP, Float, ForeignKey
from database import Base

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    id_user_1 = Column(Integer, ForeignKey('users.id'), nullable=False)
    id_user_2 = Column(Integer, ForeignKey('users.id'), nullable=False)
    id_task = Column(Integer, nullable=False)
    confirm = Column(Boolean, default=False)
    send_date = Column(TIMESTAMP, default='now()')
    completion_date = Column(TIMESTAMP, nullable=True)
    task_text= Column(String, nullable=None)
    archived = Column(Boolean, default=False)
