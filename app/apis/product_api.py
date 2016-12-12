from flask import Blueprint, jsonify

blueprint = Blueprint('product_api', __name__, url_prefix='/api/product')


@blueprint.route('/')
def index():
    return jsonify(hello='world'), 200
