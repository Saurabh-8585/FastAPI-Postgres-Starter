from sqlalchemy import (
    Column,
    String,
    Integer,
)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class MasterCity(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, index=True)
    u_name = Column(String)
    u_address = Column(String)
    u_age = Column(Integer)
