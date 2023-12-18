from .sql_db import engine, Base, session
from asyncio import run

from apps.user.models import *
from apps.product.models import *
from apps.order.models import *


def reset_database():
    run(drop_create_database())
    run(create_city_state())


async def drop_create_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def create_city_state():
    async with session() as s:
        state = Uf(abbreviation="PA", name="Philadelphia")
        s.add(state)

        await s.commit()
        city = City(name="Scranton", uf_id=state.id)
        s.add(city)

        await s.commit()
