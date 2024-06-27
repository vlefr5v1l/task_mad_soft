from pydantic import BaseModel
from typing import List

class MemeBase(BaseModel):
    text: str

class MemeCreate(MemeBase):
    image_url: str

class MemeUpdate(MemeBase):
    image_url: str

class Meme(MemeBase):
    id: int
    image_url: str

    class Config:
        orm_mode = True

class MemeList(BaseModel):
    memes: List[Meme]
