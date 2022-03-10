from sqlalchemy import Column, DateTime, Text, BigInteger, Integer
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


# Таблицы для телеграм-бота
class Users(Base):
    __tablename__ = 'Users'
    id = Column("Id", BigInteger, primary_key=True)
    user_id = Column("UserId", BigInteger)
    user_text = Column("UserText", Text)
    date = Column("Date", DateTime, default=datetime.now())
