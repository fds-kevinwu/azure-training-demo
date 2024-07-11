from sqlalchemy import String, Integer, Column
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(16), index=True)
    title = Column(String(16))
    lesson = Column(String(16))