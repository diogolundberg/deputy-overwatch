from overwatch import app
from flask.ext.runner import Manager
from flask_migrate import MigrateCommand

manager = Manager(app)
manager.add_command('db', MigrateCommand)

manager.run()
