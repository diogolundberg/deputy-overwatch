from overwatch import app
from flask.ext.runner import Manager

manager = Manager(app)
manager.run()
