from flask import Blueprint, jsonify
from overwatch.models import Indemnity

blueprint = Blueprint('indemnity_api', __name__, url_prefix='/api/indemnities')

@blueprint.route('/')
def list():
    indemnities = [dict(i) for i in Indemnity.query.all()]
    return jsonify(indemnities = indemnities), 200

@blueprint.route('/categories/deputies/')
def categories_deputies():
    return jsonify(categories = []), 200
