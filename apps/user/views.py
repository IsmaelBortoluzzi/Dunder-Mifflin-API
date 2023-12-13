from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from constants import RESPONSE_ERROR_400_BAD_REQUEST as ERROR_400
from .schemas import CreateUserReq, CreateUserRes
from . import crud

router_user = APIRouter(prefix="/user")


@router_user.post("/create/", response_model=CreateUserRes, status_code=status.HTTP_201_CREATED, responses=ERROR_400, tags=["User"])
async def create_user(user: CreateUserReq):
    user_exists = await crud.user_exists(email=user.email)

    if user_exists:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"message": "User with this email already exists!"})

    new_user = await crud.create_user(user)
    return new_user
