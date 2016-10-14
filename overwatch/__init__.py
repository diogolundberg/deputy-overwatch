from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv, listdir, getcwd
from importlib import import_module
from re import sub

app = Flask(__name__)
app.config.from_object('config.' + getenv('ENV', 'Development'))

db = SQLAlchemy(app)

controllers = [sub('\.py$', '', c) for c in listdir(getcwd()+'/overwatch/controllers') if c.endswith('_controller.py')]

for controller in controllers:
    module = import_module('overwatch.controllers.%s' % controller)
    app.register_blueprint(module.blueprint)


apis = [sub('\.py$', '', c) for c in listdir(getcwd()+'/overwatch/api') if c.endswith('_api.py')]

for api in apis:
    module = import_module('overwatch.api.%s' % api)
    app.register_blueprint(module.blueprint)