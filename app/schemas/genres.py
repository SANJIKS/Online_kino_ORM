from pydantic import BaseModel
from typing import List

class GenreCreateSchema(BaseModel):
    title: str

    class Config:
        orm_mode = True

class GenreAllSchema(BaseModel):
    title: List[str]
    
    class Config:
        orm_mode = True


