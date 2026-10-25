

from datetime import datetime

from pydantic import BaseModel,EmailStr, Field,ConfigDict
from typing import Optional



class BaseSchema(BaseModel):
    title:str
    content:str
    published:Optional[bool]=True

class CreateSchema(BaseSchema):
    pass

class ResponseSchema(BaseSchema):
    id:int
    created_at:datetime
    user_id:int
    owner:UserResponse

class postOut(BaseModel):
    Post:ResponseSchema
    votes:int
    # class Config:
    #     from_attributes = True
    model_config = ConfigDict(from_attributes=True)


# user schema
class CreateUser(BaseModel):
    email:EmailStr
    password:str

class UserResponse(BaseModel):
    id:int
    email:EmailStr
    created_at:datetime
    # class Config:
    #     from_attribuites=True
    model_config = ConfigDict(from_attributes=True)
    


class Token(BaseModel):
    token:str
    token_type:str


class token_data(BaseModel):
    id:Optional[int]=None


class Vote(BaseModel):
    post_id:int
    dir: int = Field(..., ge=-1, le=1) 