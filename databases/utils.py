from .sql_db import engine, Base, session
from .decorators import with_session
from asyncio import run

from apps.user.models import *
from apps.product.models import *
from apps.order.models import *


def reset_database():
    run(drop_create_database())
    run(create_city_state())
    run(add_products())


async def drop_create_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


@with_session(session)
async def create_city_state(s):
    state = Uf(abbreviation="PA", name="Philadelphia")
    s.add(state)

    await s.commit()
    city = City(name="Scranton", uf_id=state.id)
    s.add(city)

    await s.commit()


@with_session(session)
async def add_products(s):
    products = [
        Product(name='A4 Paper', product_variations=[
            ProductVariation(sku=101, description='Standard A4 Paper', active=True, size='A4', color='White', price=5.99),
            ProductVariation(sku=102, description='A4 Paper - Recycled', active=True, size='A4', color='Green', price=6.49),
            ProductVariation(sku=103, description='Premium A4 Paper', active=True, size='A4', color='Ivory', price=8.99),
            ProductVariation(sku=104, description='A4 Paper - Colored', active=True, size='A4', color='Blue', price=7.99),
            ProductVariation(sku=105, description='A4 Paper - Glossy', active=True, size='A4', color='Photo White', price=9.99),
        ]),
        Product(name='Legal Size Paper', product_variations=[
            ProductVariation(sku=201, description='Standard Legal Size Paper', active=True, size='Legal', color='White', price=7.49),
            ProductVariation(sku=202, description='Legal Size Paper - Recycled', active=True, size='Legal', color='Green', price=8.99),
            ProductVariation(sku=203, description='Premium Legal Size Paper', active=True, size='Legal', color='Ivory', price=10.99),
            ProductVariation(sku=204, description='Legal Size Paper - Colored', active=True, size='Legal', color='Yellow', price=9.49),
            ProductVariation(sku=205, description='Legal Size Paper - Heavyweight', active=True, size='Legal', color='Gray', price=12.99),
        ]),

        Product(name='Notebook Paper', product_variations=[
            ProductVariation(sku=301, description='Wide Ruled Notebook Paper', active=True, size='Letter', color='White', price=4.99),
            ProductVariation(sku=302, description='College Ruled Notebook Paper', active=True, size='Letter', color='Blue', price=5.49),
            ProductVariation(sku=303, description='Notebook Paper - Recycled', active=True, size='Letter', color='Green', price=6.99),
            ProductVariation(sku=304, description='Premium Notebook Paper', active=True, size='Letter', color='Ivory', price=8.49),
            ProductVariation(sku=305, description='Notebook Paper - Colored', active=True, size='Letter', color='Pink', price=7.99),
        ]),
        Product(name='Drawing Paper', product_variations=[
            ProductVariation(sku=401, description='Sketching Paper Pad', active=True, size='9x12', color='White', price=11.99),
            ProductVariation(sku=402, description='Drawing Paper - Heavyweight', active=True, size='11x14', color='Ivory', price=14.99),
            ProductVariation(sku=403, description='Watercolor Paper Pad', active=True, size='8x10', color='Cream', price=16.99),
            ProductVariation(sku=404, description='Drawing Paper - Mixed Media', active=True, size='9x12', color='Kraft', price=13.49),
            ProductVariation(sku=405, description='Charcoal Drawing Paper', active=True, size='11x17', color='Gray', price=9.99),
        ]),
        Product(name='Cardstock', product_variations=[
            ProductVariation(sku=501, description='Heavyweight Cardstock', active=True, size='Letter', color='White', price=12.99),
            ProductVariation(sku=502, description='Cardstock - Colored', active=True, size='Letter', color='Assorted', price=14.49),
            ProductVariation(sku=503, description='Premium Cardstock', active=True, size='Letter', color='Ivory', price=16.99),
            ProductVariation(sku=504, description='Cardstock - Metallic', active=True, size='Letter', color='Gold', price=18.99),
            ProductVariation(sku=505, description='Cardstock - Textured', active=True, size='Letter', color='Linen', price=15.99),
        ]),
    ]

    s.add_all(products)
    await s.commit()

