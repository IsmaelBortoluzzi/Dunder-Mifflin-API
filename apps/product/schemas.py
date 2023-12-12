from pydantic import BaseModel, Field


class Product(BaseModel):
    id: int
    name: str


class ProductVariation(BaseModel):
    id: int
    product_id: int
    sku: int
    description: str | None
    active: bool
    size: str | None
    color: str | None
    price: str | None


class ProductOrder(BaseModel):
    id: int
    product_variation_id: int
    order_id: int
    quantity: int 


