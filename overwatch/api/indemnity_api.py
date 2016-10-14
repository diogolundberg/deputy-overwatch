from flask import Blueprint, jsonify

blueprint = Blueprint('indemnity_api', __name__, url_prefix='/api/indemnities')

@blueprint.route('/')
def index():
    return jsonify(indemnities = []), 200
