from . import crud
from . import schemas
from apps.product import schemas as product_schemas
from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from constants import RESPONSE_ERROR_400_BAD_REQUEST as ERROR_400, RESPONSE_ERROR_404_NOT_FOUND as ERROR_404, MAX_PRODUCT_VARIATION_PER_PAGE


router_order = APIRouter(prefix="/order")


@router_order.post("/create/", response_model=schemas.CreateOrderRes, status_code=status.HTTP_201_CREATED, tags=["Order"])
async def create_order(order: schemas.CreateOrderReq):
    new_order = await crud.create_order(order)
    return new_order


@router_order.get("/retrieve/{order_id}/", response_model=schemas.RetrieveOrderRes, status_code=status.HTTP_200_OK, responses=ERROR_404, tags=["Order"])
async def get_order(order_id: int):
    order = await crud.get_order(id=order_id)

    if not order:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": f"Order with id {order_id} does not exist!"})

    return order 