import factory
from app import db
from app.models.product import Product
import factory

class ProductFactory(factory.alchemy.SQLAlchemyModelFactory):

    class Meta:
        model = Product
        sqlalchemy_session = db.session
 
    name =  factory.Sequence(lambda n: "Product %03d" % n)
    value = 10
 
