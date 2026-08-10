from pydantic import BaseModel, Field

class MovieReponse(BaseModel):
    id: int
    name: str
    director: str
    
