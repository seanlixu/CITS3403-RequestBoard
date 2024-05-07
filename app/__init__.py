# Imports
from flask import Flask
from flask import flash
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


# Flask app name
flaskApp = Flask(__name__)
# Setting config
flaskApp.config.from_object(Config)
# Set db to SQL of flaskapp
db = SQLAlchemy(flaskApp)

migrate = Migrate(flaskApp, db)


@flaskApp.cli.command('initdb')
def initdb_command():
    """Creates the database tables."""
    print("created")
    db.create_all()

# ... rest of your application code

# @flaskApp.route("/")
# def main():
#     return render_template('test.html')
from app import models, routes
