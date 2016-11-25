from flask_migrate import MigrateCommand
from overwatch import manager
from overwatch.scripts import Scrape

manager.add_command('db', MigrateCommand)
manager.add_command('scrape', Scrape)
manager.run()
