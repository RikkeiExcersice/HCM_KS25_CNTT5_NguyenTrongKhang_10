from sqlalchemy import Column, Integer, String, Float, ForeignKey
from database import Base
from sqlalchemy_utils import relationships

class tickets(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    ticket_code = Column(String(20), unique=True, nullable=False)
    seat_number = Column(String(10),unique=True, nullable=False)
    price = Column(Float, nullable = False)
    movie_id = Column(ForeignKey("movie.id"), nullable=False)

    movie = relationships("movie", back_populates = "tickets")