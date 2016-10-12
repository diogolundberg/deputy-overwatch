from os import getenv, listdir, getcwd
from importlib import import_module
from flask import Flask

app = Flask(__name__)
app.config.from_object('config.' + getenv('ENV', 'Development'))

modules = [module for module in listdir(getcwd()+'/overwatch/modules') if '.' not in module]

for module in modules:
    views = import_module('overwatch.modules.%s.views' % module)
    app.register_blueprint(views.mod)