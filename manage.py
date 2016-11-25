from overwatch import app, db, models
from overwatch.scripts import Scrape
from flask.ext.runner import Manager
from flask_migrate import MigrateCommand, Migrate

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)
manager.add_command('scrape', Scrape)

manager.run()
