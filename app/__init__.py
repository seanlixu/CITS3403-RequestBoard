# # Imports
# from flask import Flask
# from flask import flash
# from .config import Config
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate


# # Flask app name
# flaskApp = Flask(__name__)
# # Setting config
# flaskApp.config.from_object(Config)
# # Set db to SQL of flaskapp
# db = SQLAlchemy(flaskApp)

# migrate = Migrate(flaskApp, db)


# @flaskApp.cli.command('initdb')
# def initdb_command():
#     """Creates the database tables."""
#     print("created")
#     db.create_all()

# # ... rest of your application code

# # @flaskApp.route("/")
# # def main():
# #     return render_template('test.html')
# from app import models, routes
# Imports

# Imports
from flask import Flask
from flask import flash
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


# Flask app name
flaskApp = Flask(__name__)
# Setting config
flaskApp.config.from_object(Config)
# Set db to SQL of flaskapp
db = SQLAlchemy(flaskApp)

migrate = Migrate(flaskApp, db)

login_manager = LoginManager()  # Add this line
login_manager.init_app(flaskApp)  # Add this line

@login_manager.user_loader  # Add this line
def load_user(user_id):  # Add this line
    return User.query.get(int(user_id))  # Add this line

# FOR testing and create db
@flaskApp.cli.command('initdb')
def initdb_command():
    """Creates the database tables."""
    print("created")
    db.create_all()



# @flaskApp.route("/")
# def main():
#     return render_template('test.html')

from .models import User  # Move this line to the end
from app import models, routes

