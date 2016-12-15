from flask import Blueprint, jsonify
from app.models.product import Product

blueprint = Blueprint('product_api', __name__, url_prefix='/api/product')


@blueprint.route('/')
def index():
    products = Product.query.all()
    data = []
    columns = []
    if products:
        columns = list(dict(products[0]).keys())
        data = [list(dict(x).values()) for x in products]
    return jsonify(columns=columns, data=data)
