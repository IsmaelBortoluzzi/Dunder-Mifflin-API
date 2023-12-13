from pydantic import BaseModel, Field, EmailStr
from datetime import datetime


####### USER MODELS #######


class User(BaseModel):
    id: int
    full_name: str
    email: EmailStr
    password: str
    active: bool
    create_date: datetime
    update_date: datetime


class CreateUserReq(BaseModel):
    full_name: str = Field(example="Dwight Schrute")
    email: EmailStr = Field(example="schrute@schrutefarms.com")
    password: str = Field(example="BEET")


class CreateUserRes(BaseModel):
    id: int
    full_name: str
    email: EmailStr
    create_date: datetime


class RetrieveUserRes(BaseModel):
    id: int
    full_name: str
    email: EmailStr
    active: bool
    create_date: datetime
    update_date: datetime | None


class UpdateUserReq(BaseModel):
    full_name: str | None
    email: EmailStr | None
    password: str | None


class UpdateUserRes(BaseModel):
    id: int
    full_name: str
    email: EmailStr
    active: bool
    create_date: datetime
    update_date: datetime


####### END USER MODELS #######

class Uf(BaseModel):
    id: int  
    abbreviation: str = Field(example='SC')
    name: str = Field(example='Santa Catarina')


class City(BaseModel):
    id: int
    name: str
    uf_id: int


class Address(BaseModel):
    id: int
    number: str = Field(example='1045')
    street_name: str
    zip_code: str
    city_id: int
    user_id: int
