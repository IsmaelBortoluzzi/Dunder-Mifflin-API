from sqlalchemy import Column, ForeignKey, Integer, String, Double, DateTime
from sqlalchemy.orm import relationship
from databases.sql_db import Base, session
from sqlalchemy.sql import functions
from sqlalchemy.future import select
from apps.product.models import ProductVariation

import datetime


class Order(Base):
    __tablename__ = "order"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    total = Column(Double(precision=8), nullable=True)
    obs = Column(String(length=1024), default="")
    create_date = Column(DateTime, default=datetime.datetime.now())
    update_date = Column(DateTime, nullable=True)
    delivery_address_id = Column(Integer, ForeignKey("address.id"))
    status = Column(String(length=32))

    products = relationship("ProductVariation", secondary="product_order", back_populates="orders")
    user = relationship("User", back_populates="orders")
    delivery_address = relationship("Address", back_populates="orders", lazy="joined")

    STATUS_CHOICES = ["Cancelled", "New", "In Process", "Shipped", "Complete"]

    async def calculate_total(self):
        async with session() as s:   
            query = await s.execute(
                select(functions.sum(ProductVariation.price))
                    .join(Order.products)
                    .where(Order.id == self.id)
                    .group_by(Order.id)
            )
            return query.first()[0]


    def set_status(self, label):
        for status in self.STATUS_CHOICES:
            if status == label:
                self.status = status
                break
        else:
            raise ValueError(f'There are no status with label "{label}"')
        

