from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from databases.utils import reset_database
from apps.user.views import router_user


# reset_database()

tags_metadata = [
    {
        "name": "User",
        "description": "Operations with users, login and adresses"
    },
    {
        "name": "Order",
        "description": "Operations with order"
    },
    {
        "name": "Product",
        "description": "Operations with products"
    }
]

app = FastAPI(
    title="Dunder Mifflin API",
    description="Modern Dunder Mifflin Backend System To Keep Up With Market Changes",
    redoc_url='/',
    openapi_tags=tags_metadata
)

origins = [
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["get", "post", "patch", "put", "delete"]
)

app.include_router(router_user)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)

# RUN
# uvicorn main:app --reload

