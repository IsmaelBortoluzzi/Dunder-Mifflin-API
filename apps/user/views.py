from . import crud
from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from .schemas import CreateUserReq, CreateUserRes, RetrieveUserRes, UpdateUserReq, UpdateUserRes
from constants import RESPONSE_ERROR_400_BAD_REQUEST as ERROR_400, \
                      RESPONSE_ERROR_404_NOT_FOUND as ERROR_404


router_user = APIRouter(prefix="/user")


@router_user.post("/create/", response_model=CreateUserRes, status_code=status.HTTP_201_CREATED, responses=ERROR_400, tags=["User"])
async def create_user(user: CreateUserReq):
    user_exists = await crud.user_exists(email=user.email)

    if user_exists:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"message": "User with this email already exists!"})

    new_user = await crud.create_user(user)
    return new_user


@router_user.post("/retrieve/{user_id}", response_model=RetrieveUserRes, status_code=status.HTTP_200_OK, responses=ERROR_404, tags=["User"])
async def get_user(user_id: int):
    user = await crud.get_user(id=user_id)

    if not user:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "User does't exists!"})

    return user 


@router_user.post("/update/{user_id}", response_model=UpdateUserRes, status_code=status.HTTP_200_OK, responses=ERROR_404, tags=["User"])
async def update_user(user_id: int, user: UpdateUserReq):
    user_exists = await crud.user_exists(id=user_id)

    if not user_exists:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "User does't exists!"})

    updated_user = await crud.update_user(id=user_id, user=user)

    return updated_user 


