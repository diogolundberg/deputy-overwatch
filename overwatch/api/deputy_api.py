from flask import Blueprint, jsonify

blueprint = Blueprint('deputy_api', __name__, url_prefix='/api/deputies')

@blueprint.route('/')
def list():
    return jsonify(deputies = []), 200
