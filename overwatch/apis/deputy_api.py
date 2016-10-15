from flask import Blueprint, jsonify
from overwatch.models import Deputy

blueprint = Blueprint('deputy_api', __name__, url_prefix='/api/deputies')

@blueprint.route('/')
def list():
    deputies = [dict(d) for d in Deputy.query.all()]
    return jsonify(deputies = deputies), 200
