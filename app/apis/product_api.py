from flask import Blueprint, jsonify

blueprint = Blueprint('product_api', __name__, url_prefix='/api/product')


@blueprint.route('/')
def index():
    return jsonify(columns=["product", "value"], data=[1,1,1,1,1,1,1,1,1,1])
