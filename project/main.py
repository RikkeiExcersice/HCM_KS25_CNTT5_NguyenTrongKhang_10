from fastapi import FastAPI, Depends
from database import Base, get_db
from sqlalchemy import engine
from sqlalchemy.orm import Session
from schemas.ticket import *
from models.ticket import *
app = FastAPI()



@app.get("/health")
def check_health_db():
    return {
        "message" : "Oke..."
    }

@app.get("/tickets")
def get_tickets(db: Session = Depends(get_db)):
    db.query(tickets).all