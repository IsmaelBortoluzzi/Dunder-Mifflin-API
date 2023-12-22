from typing import List
from pydantic import BaseModel, Field
from datetime import datetime
from apps.product import schemas as product_schemas
from apps.user.schemas import Address


class Order(BaseModel):
    id: int
    user_id: int
    total: float
    obs: str
    create_date: datetime
    update_date: datetime
    delivery_address_id: int
    status: str


class CreateOrderReq(BaseModel):
    user_id: int = Field(example=1)
    obs: str = Field(example="BEETS GONNA BEAT")
    delivery_address_id: int = Field(example=1)
    products: List[int] = Field(example=[1, 3, 4, 7])  # list of ProductVariation.id


class CreateOrderRes(BaseModel):
    id: int
    user_id: int
    total: float
    obs: str
    create_date: datetime
    delivery_address_id: int
    status: str


class RetrieveOrderRes(BaseModel):
    id: int
    user_id: int
    total: float
    obs: str
    create_date: datetime
    update_date: datetime | None
    address: Address
    status: str
    product_list: List[product_schemas.ProductVariation]
