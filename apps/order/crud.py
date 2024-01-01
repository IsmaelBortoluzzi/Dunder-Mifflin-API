import datetime
from sqlalchemy.future import select
from sqlalchemy import update, delete
from databases.sql_db import session
from databases.decorators import with_session
from .models import Order
from apps.product.models import ProductOrder, ProductVariation
from apps.product.crud import get_product_order


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
async def order_exists(s, id=None):
    if id:
        exists_query = select(Order).where(Order.id == id).exists()
    else:
        raise ValueError('You must pass "id" parameter')

    query = await s.execute(select(Order).where(exists_query))
    return query.first()


@with_session(session)
async def get_order(s, id=None):
    if not id:
        raise ValueError('You must pass "id" parameter')

    query = await s.execute(
        select(Order).where(Order.id == id)
    )

    return query.scalar()


async def add_product(order_id, product):
    await _add_product(order_id, product)
    order = await _update_order_total(order_id)

    return order


@with_session(session)
async def _add_product(s, order_id, product):
    new_product_order = ProductOrder(order_id=order_id, product_variation_id=product.product_variation_id, quantity=product.quantity)
    product_order = await get_product_order(new_product_order.order_id, new_product_order.product_variation_id)

    if product_order:
        await s.execute(
            update(ProductOrder)
                .where(ProductOrder.id == product_order.id)
                .values(quantity=product_order.quantity + new_product_order.quantity)
        )
    else:
        s.add(new_product_order)

    await s.commit()


async def remove_product(order_id, product):
    await _remove_product(order_id, product)
    order = await _update_order_total(order_id)

    return order


@with_session(session)
async def _remove_product(s, order_id, product):
    product_order = await get_product_order(order_id, product.product_variation_id)

    if not product_order:
        return

    if product_order.quantity - product.quantity <= 0:
        await s.execute(
                delete(ProductOrder)
                    .where(ProductOrder.id == product_order.id)
            )
    else:
        await s.execute(
            update(ProductOrder)
                .where(ProductOrder.id == product_order.id)
                .values(quantity=product_order.quantity - product.quantity)
        )

    await s.commit()


@with_session(session)
async def _update_order_total(s, order_id):
    order = await get_order(id=order_id)
    order.total = await order.calculate_total()
    order.update_date = datetime.datetime.now()

    await s.execute(
        update(Order)
            .where(Order.id == order.id)
            .values(total=order.total, update_date=order.update_date)
    )
    await s.commit()

    return order
