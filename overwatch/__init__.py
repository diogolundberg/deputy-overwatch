from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv, listdir, getcwd, path
from importlib import import_module
from re import sub
from pattern.en import pluralize, singularize

app = Flask(__name__)
app.config.from_object('config.' + getenv('ENV', 'Development'))

db = SQLAlchemy(app)

def import_modules(package):
    package_dir = path.join(getcwd(), __name__, package)
    module_suffix = '_'+singularize(package)+'.py'

    module_names = [sub('\.py$', '', c) for c in listdir(package_dir) if c.endswith(module_suffix)]

    for module_name in module_names:
        module = import_module('overwatch.%s.%s' % (package, module_name))
        app.register_blueprint(module.blueprint)

import_modules('controllers')
import_modules('apis')