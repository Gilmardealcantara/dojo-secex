import factory
from app import db
from app.models.product import Product


class ProductFactory(factory.alchemy.SQLAlchemyModelFactory):

    class Meta:
        model = Product
        sqlalchemy_session = db.session
 
    name =  "produtox"
    value = 10
 
