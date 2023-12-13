from sqlalchemy import Column, ForeignKey, Integer, String, Double, DateTime
from sqlalchemy.orm import relationship
from databases.sql_db import Base
import datetime


class Order(Base):
    __tablename__ = 'order'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    total = Column(Double(precision=8))
    obs = Column(String(length=1024), default='')
    create_date = Column(DateTime, default=datetime.datetime.now())
    update_date = Column(DateTime, nullable=True)
    
    products = relationship('ProductVariation', secondary='product_order', back_populates='orders')
    user = relationship('User', back_populates='orders')


    def calculate_total(self):
        pass
