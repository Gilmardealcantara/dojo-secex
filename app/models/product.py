from sqlalchemy import Column, Integer, String, BigInteger
from app import db


class Product(db.Model):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    value = Column(Integer)

    def __iter__(self):
        yield 'id', self.id
        yield 'name', self.name
        yield 'value', self.value
