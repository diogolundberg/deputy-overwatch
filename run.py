from overwatch import app
from flask.ext.runner import Manager

@app.route("/")
def index():
    return 'Hello World'

manager = Manager(app)
manager.run()
