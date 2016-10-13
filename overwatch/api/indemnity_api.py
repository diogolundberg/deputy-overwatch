from flask import Blueprint, jsonify

blueprint = Blueprint('indemnity_api', __name__, url_prefix='/api/indemnity')

@blueprint.route('/')
def index():
    return jsonify(indemnities = []), 200
