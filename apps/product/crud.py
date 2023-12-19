from sqlalchemy.future import select
from sqlalchemy import delete
from databases.sql_db import session
from databases.decorators import with_session
from .models import Product, ProductVariation


@with_session(session)
async def product_exists(s, id=None):
    if id:
        exists_query = select(Product).where(Product.id == id).exists()
    else:
        raise ValueError('You must pass "id" parameter')

    query = await s.execute(select(Product).where(exists_query))
    return query.first()


@with_session(session)
async def create_product(s, product):
    new_product = Product(**product.dict())

    s.add(new_product)
    await s.commit()

    return new_product


@with_session(session)
async def delete_product(s, id=None):
    if id is None:
        raise ValueError('You must pass "id" parameter')

    await s.execute(delete(Product).where(Product.id == id))
    await s.commit()


@with_session(session)
async def product_variation_exists(s, id=None):
    if id:
        exists_query = select(ProductVariation).where(ProductVariation.id == id).exists()
    else:
        raise ValueError('You must pass "id" parameter')

    query = await s.execute(select(ProductVariation).where(exists_query))
    return query.first()


@with_session(session)
async def create_product_variation(s, product_variation):
    new_product_variation = ProductVariation(**product_variation.dict())

    s.add(new_product_variation)
    await s.commit()

    return new_product_variation


@with_session(session)
async def delete_product_variation(s, id=None):
    if id is None:
        raise ValueError('You must pass "id" parameter')

    await s.execute(delete(ProductVariation).where(ProductVariation.id == id))
    await s.commit()


@with_session(session)
async def list_product_variation(s, skip, limit):
    products = await s.execute(
        select(ProductVariation).order_by(ProductVariation.id).offset(skip).limit(limit)
    )

    return products.all()