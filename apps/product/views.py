from . import crud
from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from .schemas import CreateProductReq, Product, ProductVariation, CreateProductVariationReq
from constants import RESPONSE_ERROR_400_BAD_REQUEST as ERROR_400, RESPONSE_ERROR_404_NOT_FOUND as ERROR_404, MAX_PRODUCT_VARIATION_PER_PAGE
from typing import List


router_product = APIRouter(prefix="/product")


@router_product.post("/create/", response_model=Product, status_code=status.HTTP_201_CREATED, tags=["Product"])
async def create_product(product: CreateProductReq):
    new_product = await crud.create_product(product)
    return new_product


@router_product.delete("/delete/{product_id}/", status_code=status.HTTP_204_NO_CONTENT, responses=ERROR_404, tags=["Product"])
async def delete_product(product_id: int):
    product_exists = await crud.product_exists(product_id)

    if not product_exists:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "Product does't exist!"})

    await crud.delete_product(product_id)


@router_product.post("/variation/create/", response_model=ProductVariation, status_code=status.HTTP_201_CREATED, responses=ERROR_400, tags=["Product"])
async def create_product_variation(product_variation: CreateProductVariationReq):
    product_exists = await crud.product_exists(id=product_variation.product_id)

    if not product_exists:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"message": "Product does not exist!"})

    new_product_variation = await crud.create_product_variation(product_variation)
    return new_product_variation


@router_product.delete("/variation/delete/{product_variation_id}/", status_code=status.HTTP_204_NO_CONTENT, responses=ERROR_404, tags=["Product"])
async def delete_product_variation(product_variation_id: int):
    product_variation_exists = await crud.product_variation_exists(id=product_variation_id)

    if not product_variation_exists:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "Product does't exist!"})

    await crud.delete_product_variation(product_variation_id)


@router_product.get("/variation/list/", response_model=List[ProductVariation], status_code=status.HTTP_200_OK, responses=ERROR_400, tags=["Product"])
async def list_product_variation(skip: int = 0, limit: int = 5):
    if skip >= limit:
        return []

    if limit - skip > MAX_PRODUCT_VARIATION_PER_PAGE:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"message": f"Product range exceded {MAX_PRODUCT_VARIATION_PER_PAGE}"})

    return await crud.list_product_variation(skip, limit) 
