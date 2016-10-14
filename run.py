from overwatch import app, db, models
from flask.ext.runner import Manager
from flask_migrate import MigrateCommand, Migrate

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

manager.run()
