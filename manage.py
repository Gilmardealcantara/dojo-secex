from app import manager
from flask_migrate import MigrateCommand
from scripts.load_data import LoadData

manager.add_command('db', MigrateCommand)
manager.add_command('load', LoadData)
manager.run()
