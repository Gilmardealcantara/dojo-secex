from flask_migrate import MigrateCommand
from app import manager

manager.add_command('db', MigrateCommand)
manager.run()
