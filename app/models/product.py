from sqlalchemy import Column, Integer, String, BigInteger
from app import db


class Product(db.Model):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    product = Column(String)
    value = Column(Integer)

    def __iter__(self):
        yield 'product', self.product
        yield 'value', self.value