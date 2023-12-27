from typing import List
from pydantic import BaseModel, Field


class Product(BaseModel):
    id: int
    name: str


class CreateProductReq(BaseModel):
    name: str = Field(example="A4 Paper")


class ListProductRes(BaseModel):
    skip: int
    limit: int
    products: List[Product]


class ProductVariation(BaseModel):
    id: int
    product_id: int
    sku: int
    description: str | None
    active: bool
    size: str | None
    color: str | None
    price: float


class ProductVariationWithProduct(BaseModel):
    id: int
    product: Product
    sku: int
    description: str | None
    active: bool
    size: str | None
    color: str | None
    price: float


class ListProductVariationRes(BaseModel):
    skip: int
    limit: int
    products: List[ProductVariation]


class CreateProductVariationReq(BaseModel):
    product_id: int = Field(example=1)
    sku: int = Field(example="12345")
    description: str | None = Field(example="Paper for printing")
    active: bool = Field(example=True)
    size: str | None = Field(example="20x30")
    color: str | None = Field(example=None)
    price: float = Field(example=20.99)


class ProductOrder(BaseModel):
    id: int
    product_variation_id: int
    order_id: int
    quantity: int 


