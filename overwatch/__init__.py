from os import getenv
from flask import Flask

app = Flask(__name__)
app.config.from_object('config.' + getenv('ENV', 'Development'))

@app.route("/")
def index():
    return 'Hello World', 200
