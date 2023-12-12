from pydantic import BaseModel, Field
from datetime import datetime


class User(BaseModel):
    id: int
    full_name: str
    email: str
    password: str
    active: bool
    create_date: datetime
    update_date: datetime


class Uf(BaseModel):
    id: int  
    abbreviation: str = Field(examples='SC')
    name: str = Field(examples='Santa Catarina')


class City(BaseModel):
    id: int
    name: str
    uf_id: int


class Address(BaseModel):
    id: int
    number: str = Field(examples='1045')
    street_name: str
    zip_code: str
    city_id: int
    user_id: int
