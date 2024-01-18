from sqlalchemy import create_engine
import os
from src.db.models import Base
from sqlalchemy.orm import sessionmaker

engine = None
SessionMaker = None


def get_session():
    """
    Obtains a session object from SessionMaker and assigns it to the session variable
    """
    if SessionMaker is not None:
        session = SessionMaker()
        return session
    else:
        return None


def connect_db():
    POSTGRES_USER = 'postgres'
    POSTGRES_PASSWORD = 'password'
    POSTGRES_SERVER = '10.129.2.45'
    POSTGRES_PORT = '5432'
    POSTGRES_DB = 'test_my_db'

    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"
    global engine, SessionMaker
    engine = create_engine(
        DATABASE_URL,
        connect_args={"connect_timeout": 2},
        pool_size=0,
        max_overflow=-1,
        pool_recycle=3600,
    )
    engine.connect()
    SessionMaker = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    # create all the tables if not already there
    Base.metadata.create_all(engine)

    return True
