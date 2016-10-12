from flask import Blueprint

mod = Blueprint('home', __name__, url_prefix='/')

@mod.route('/')
def index():
    return 'Hello World', 200
