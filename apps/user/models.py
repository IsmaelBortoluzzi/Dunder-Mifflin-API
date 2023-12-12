from sqlalchemy import Column, ForeignKey, Integer, String, Double, DateTime, Boolean
from sqlalchemy.orm import relationship
from databases.sql_db import Base
import datetime


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    full_name = Column(String(length=64))
    email = Column(String(length=128))
    password = Column(String(length=64))
    active = Column(Boolean, default=True)
    create_date = Column(DateTime, default=datetime.datetime.now())
    update_date = Column(DateTime, nullable=True)
    
    orders = relationship('Order', back_populates='user')
    addresses = relationship('Address', back_populates='user')

    def check_password(self, password):
        pass

    def set_password(self, password):
        pass


class Uf(Base):
    __tablename__ = 'uf'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    abbreviation = Column(String(length=2))
    name = Column(String(length=128))

    citis = relationship('City', back_populates='uf')


class City(Base):
    __tablename__ = 'city'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(length=128))
    uf_id = Column(Integer, ForeignKey('uf.id'))

    uf = relationship('Uf', back_populates='city')
    addresses = relationship('Address', back_populates='city')


class Address(Base):
    __tablename__ = 'address'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    number = Column(String(length=8))
    street_name = Column(String(length=128))
    zip_code = Column(String(length=16))
    city_id = Column(Integer, ForeignKey('city.id'))
    user_id = Column(Integer, ForeignKey('user.id'))

    city = relationship('City', back_populates='address')
    user = relationship('User', back_populates='address')

