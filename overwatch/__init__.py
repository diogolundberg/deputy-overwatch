from os import getenv
from flask import Flask
from overwatch.modules.home .views import mod as home

app = Flask(__name__)
app.config.from_object('config.' + getenv('ENV', 'Development'))

app.register_blueprint(home)
