from pydantic import BaseModel, Field

class TicketCreate(BaseModel):
    ticket_code:int = Field(min_length=6, max_length=20)
    seat_number:str = Field(min_length=6, max_length = 10)
    price:float = Field(gt = 0)
    movie_id : int

class TicketResponse(BaseModel):
    id: int
    ticket_code: str
    seat_number: str
    price: float


    
