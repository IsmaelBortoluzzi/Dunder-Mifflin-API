import datetime
from sqlalchemy.future import select
from sqlalchemy import delete
from databases.sql_db import session
from databases.decorators import with_session
from .models import Order
from apps.product.models import ProductOrder, ProductVariation


@with_session(session)
async def order_exists(s, id=None):
    if id:
        exists_query = select(Order).where(Order.id == id).exists()
    else:
        raise ValueError('You must pass "id" parameter')

    query = await s.execute(select(Order).where(exists_query))
    return query.first()


@with_session(session)
async def create_order(s, order):
    product_variations = order.products
    del order.products

    new_order = Order(**order.dict())
    new_order.create_date = datetime.datetime.now()
    new_order.set_status("New")

    s.add(new_order)
    await s.commit()
    await s.refresh(new_order)

    product_order = map(lambda x: ProductOrder(order_id=new_order.id, product_variation_id=x.product_variation_id, quantity=x.quantity), product_variations)

    s.add_all(product_order)
    await s.commit()

    new_order.total = await new_order.calculate_total()
    await s.flush()
    await s.commit()

    return new_order


@with_session(session)
async def get_order(s, id=None):
    if not id:
        raise ValueError('You must pass "id" parameter')

    order = await s.execute(
        select(Order).where(Order.id == id)
    )

    return order.scalar()
