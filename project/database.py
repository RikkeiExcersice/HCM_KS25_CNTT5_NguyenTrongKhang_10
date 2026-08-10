from sqlalchemy import engine, create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase


DATABASE_URL = "mysql+pymysql://root:Trongkhang2007@localhost:3306/movie_ticket_db"
engine = create_engine(DATABASE_URL)

sessionLocal = sessionmaker(
    bind = engine,
    autoflush = False,
    autocommit = False
)
class Base(DeclarativeBase):
    pass

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()  