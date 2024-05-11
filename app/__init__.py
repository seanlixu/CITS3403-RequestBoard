from flask import Flask
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


flaskApp = Flask(__name__)

flaskApp.config.from_object(Config)

login = LoginManager(flaskApp)
login.login_view = 'login'
login.login_message_category = 'info'

db = SQLAlchemy(flaskApp)
migrate = Migrate(flaskApp, db)

# FOR testing and create db
@flaskApp.cli.command('initdb')
def initdb_command():
    """Creates the database tables."""
    print("created")
    db.create_all()
from app import models, routes