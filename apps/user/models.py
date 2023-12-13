from sqlalchemy import Column, ForeignKey, Integer, String, Double, DateTime, Boolean
from sqlalchemy.orm import relationship
from databases.sql_db import Base
from passlib.hash import pbkdf2_sha256 as sha256
import datetime


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    full_name = Column(String(length=64))
    email = Column(String(length=128), unique=True)
    password = Column(String(length=64))
    active = Column(Boolean, default=True)
    create_date = Column(DateTime, default=datetime.datetime.now())
    update_date = Column(DateTime, nullable=True)
    
    orders = relationship("Order", back_populates="user")
    addresses = relationship("Address", back_populates="user")

    def check_password(self, password):
        return self.password == sha256.hash(password, rounds=3000, salt_size=16)

    def set_password(self, password):
        self.password = sha256.hash(password, rounds=3000, salt_size=16)
    
    def __repr__(self):
        return f"User(id={self.id}, fullname={self.full_name})"


class Uf(Base):
    __tablename__ = "uf"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    abbreviation = Column(String(length=2))
    name = Column(String(length=128))

    cities = relationship("City", back_populates="uf")

    def __repr__(self):
        return f"Uf(id={self.id}, abbreviation={self.abbreviation})"


class City(Base):
    __tablename__ = "city"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(length=128))
    uf_id = Column(Integer, ForeignKey("uf.id"))

    uf = relationship("Uf", back_populates="cities")
    addresses = relationship("Address", back_populates="city")

    def __repr__(self):
        return f"City(id={self.id}, name={self.name})"


class Address(Base):
    __tablename__ = "address"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    number = Column(String(length=8))
    street_name = Column(String(length=128))
    zip_code = Column(String(length=16))
    city_id = Column(Integer, ForeignKey("city.id"))
    user_id = Column(Integer, ForeignKey("user.id"))

    city = relationship("City", back_populates="addresses")
    user = relationship("User", back_populates="addresses")
    orders = relationship("Order", back_populates="delivery_address")

    def __repr__(self):
        return f"Address(user_id={self.user_id}), {self.city.name}, {self.city.uf.abbreviation}"
