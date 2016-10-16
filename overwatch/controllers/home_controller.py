from flask import Blueprint

blueprint = Blueprint('home_controller', __name__, url_prefix='/')


@blueprint.route('/')
def index():
    return 'Hello World', 200
