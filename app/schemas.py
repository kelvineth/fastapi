from pydantic import BaseModel,EmailStr
from datetime import datetime
from typing import Optional
from pydantic.types import conint
class PostBase(BaseModel):
    title:str
    content:str
    published:bool = True

class Postcreate(PostBase):
    pass

class sendOut(BaseModel):
    email:EmailStr
    created:datetime
    id:int

    class Config():
        orm_mode=True

class Post(PostBase):
    id:int
    created:datetime
    owner_id:int
    owner:sendOut

    class Config():
        orm_mode=True

class Post0ut(PostBase):
    Post:Post
    Votes:int

    class Config:
        orm_mode=True


class User(BaseModel):
    email:EmailStr
    password:str



class Login(BaseModel):
    email:EmailStr
    password:str

class Token(BaseModel):
    access_token:str
    token_type:str

class TokenData(BaseModel):
    id:Optional[str] =None

class Votes(BaseModel):
    post_id:str
    dir:conint(le=1)

    
