from flask import Blueprint, jsonify

blueprint = Blueprint('hello_api', __name__, url_prefix='/api/hello')


@blueprint.route('/')
def index():
    return jsonify(hello='world'), 200
