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


class CreateOrderReqProducts(BaseModel):
    product_variation_id: int = Field(example=1)
    quantity: int = Field(example=3)


class CreateOrderReq(BaseModel):
    user_id: int = Field(example=1)
    obs: str = Field(example="BEETS GONNA BEAT")
    delivery_address_id: int = Field(example=1)
    products: List[CreateOrderReqProducts] = Field(example=[CreateOrderReqProducts(product_variation_id=3, quantity=5)])


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
    delivery_address: Address
    status: str
    products: List[product_schemas.ProductVariationWithProduct]
