import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, 'users.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "not-very-secret"
    # SECRET_KEY = os.environ.get("FLASK_SECRET_KEY")