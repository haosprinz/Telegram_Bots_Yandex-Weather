from sqlalchemy import Column, DateTime, Text, BigInteger, Float, ForeignKey, ForeignKeyConstraint
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


# Таблицы для телеграм-бота
class Dialogs(Base):
    __tablename__ = "Dialogs"
    id = Column("Id", BigInteger, primary_key=True)
    user_text = Column("UserText", Text)
    date = Column("Date", DateTime, default=datetime.now())
    users_id = Column("RolesId", BigInteger, ForeignKey("Users.Id"), nullable=True)

    Users = relationship("Users", overlaps="Dialogs")
    ForeignKeyConstraint(["users_id"], ["Users.Id"])


# Таблица пользователей
class Users(Base):
    __tablename__ = "Users"
    id = Column("Id", BigInteger, primary_key=True)
    user_id = Column("UserId", BigInteger)
    user_name = Column("UserName", Text)
    is_admin = Column("IsAdmin", bool)


# Таблица координат в системе
class Сoordinates(Base):
    __tablename__ = "Сoordinates"
    id = Column("Id", BigInteger, primary_key=True)
    name = Column("Name", Text)
    longtitude = Column("Longtitude", Float)
    latitude = Column("Latitude", Float)


# Таблица личных координат
class PersonalСoordinates(Base):
    __tablename__ = "PersonalСoordinates"
    id = Column("Id", BigInteger, primary_key=True)
    name = Column("Name", Text)
    longtitude = Column("Longtitude", Float)
    latitude = Column("Latitude", Float)
    users_id = Column("RolesId", BigInteger, ForeignKey("Users.Id"), nullable=True)

    Users = relationship("Users", overlaps="PersonalСoordinates")
    ForeignKeyConstraint(["users_id"], ["Users.Id"])


# Таблица для кэширования запросов к яндекс Апи
class RequestsCache(Base):
    __tablename__ = "RequestsCache"
    id = Column("Id", BigInteger, primary_key=True)
    #Разобрать Апи Яндекс
