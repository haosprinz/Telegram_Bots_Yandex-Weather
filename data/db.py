from sqlalchemy.sql import ClauseElement
from data.models import Base
from data.config import ENGINE, DB_NAME, CREATEBDENGINE


def get(session, model, **kwargs):
    instance = session.query(model).filter_by(**kwargs).first()
    if instance:
        return instance
    else:
        return None


def get_or_create(session, model, **kwargs):
    instance = session.query(model).filter_by(**kwargs).first()
    if instance:
        return instance, False
    else:
        params = dict((k, v) for k, v in kwargs.items() if not isinstance(v, ClauseElement))
        instance = model(**params)
        session.add(instance)
        session.flush()
        return instance, True


def drop_tables():
    Base.metadata.drop_all(ENGINE)


def create_tables():
    Base.metadata.create_all(ENGINE)


def create_db():
    with CREATEBDENGINE.connect() as connection:
        connection.execute("commit")
        connection.execute("CREATE DATABASE " + DB_NAME)
    connection.close()
