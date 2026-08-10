from sqlalchemy import Column, Integer, String
from database import Base
from sqlalchemy_utils import relationships

class movie(Base):
    id = Column(Integer, primary_key = True, autoincrement=True)
    name = Column(String(100), unique=True, nullable=False)
    director = Column(String(100), nullable=False)

    tickets = relationships("ticket", back_populates = "movie")
