from sqlalchemy import Column, ForeignKey, Integer, String, Double, DateTime
from sqlalchemy.orm import relationship
from databases.sql_db import Base
import datetime


class Order(Base):
    __tablename__ = "order"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    total = Column(Double(precision=8))
    obs = Column(String(length=1024), default="")
    create_date = Column(DateTime, default=datetime.datetime.now())
    update_date = Column(DateTime, nullable=True)
    delivery_address_id = Column(Integer, ForeignKey("address.id"))
    status = Column(Integer)
    products = relationship("ProductVariation", secondary="product_order", back_populates="orders")
    user = relationship("User", back_populates="orders")
    delivery_address = relationship("Address", back_populates="orders", lazy="joined")

    STATUS_CHOICES = [(0, "Cancelled"), (1, "New"), (2, "In Process"), (3, "Shipped"), (4, "Complete")]

    def calculate_total(self):
        pass
    