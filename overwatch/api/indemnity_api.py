from flask import Blueprint, jsonify

blueprint = Blueprint('indemnity_api', __name__, url_prefix='/api/indemnities')

@blueprint.route('/')
def list():
    return jsonify(indemnities = []), 200

@blueprint.route('/categories/deputies/')
def categories_deputies():
    return jsonify(categories = []), 200
