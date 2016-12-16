from flask import Blueprint, jsonify
from app.models.secex_2016_exp import SecexExp

blueprint = Blueprint('secex_api', __name__, url_prefix='/api/secex')


@blueprint.route('/')
def index():
    products = SecexExp.query.all()
    data = []
    columns = []
    # if products:
    #     columns = list(dict(products[0]).keys())
    #     data = [list(dict(x).values()) for x in products]
    return jsonify(columns=columns, data=data)
