from .sql_db import engine, Base
from asyncio import run

from apps.user.models import *
from apps.product.models import *
from apps.order.models import *


def reset_database():
    run(drop_create_database())


async def drop_create_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


