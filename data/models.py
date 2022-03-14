from sqlalchemy import Column, DateTime, Text, BigInteger, Integer
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


# Таблицы для телеграм-бота
class Dialogs(Base):
    __tablename__ = 'Dialogs'
    id = Column("Id", BigInteger, primary_key=True)
    user_id = Column("UserId", BigInteger)
    user_name = Column("UserName", Text)
    user_text = Column("UserText", Text)
    date = Column("Date", DateTime, default=datetime.now())
