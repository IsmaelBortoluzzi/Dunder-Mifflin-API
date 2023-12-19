from sqlalchemy import Column, ForeignKey, Integer, String, Double, DateTime, Text, Boolean, Float
from sqlalchemy.orm import relationship
from databases.sql_db import Base, session
from databases.decorators import with_session


class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(length=1024))
    
    product_variations = relationship('ProductVariation', back_populates='product')

    def __repr__(self):
        return f"Product(id={self.id}, name={self.name})"


class ProductVariation(Base):
    __tablename__ = 'product_variation'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey('product.id'), index=True)
    sku = Column(Integer, index=True)
    description = Column(Text, nullable=True)
    active = Column(Boolean, default=True)
    size = Column(String(length=32), nullable=True)
    color = Column(String(length=32), nullable=True)
    price = Column(Double(precision=8))

    product = relationship('Product', back_populates='product_variations', lazy="joined")
    orders = relationship('Order', secondary='product_order', back_populates='products')

    def __repr__(self):
        return f"ProductVariation(id={self.id}, sku={self.sku}, product_id={self.product_id})"


class ProductOrder(Base):
    __tablename__ = 'product_order'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    product_variation_id = Column(Integer, ForeignKey('product_variation.id'))
    order_id = Column(Integer, ForeignKey('order.id'))
    
    quantity = Column(Integer)


