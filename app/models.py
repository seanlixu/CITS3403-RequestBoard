from flask import Flask

import datetime, base64, os
from datetime import timedelta
from flask_login import LoginManager, flask_oauth
from flask import request, render_template, jsonify, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app import db


app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)


# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    rating = db.Column(db.Float(5.0), default=0.0)
    ratings_count = db.Column(db.Integer(), default=0)
    token = db.Column(db.DateTime)

    def get_token(self, expires_in):
        now = datetime.now()
        self.token = base64.b64encode(os.urandom(24)).decode('utf-8')
        self.token_expiration = now + timedelta(seconds=expires_in)
        db.session.add(self)
        return self.token
    
    def revoke_token(self):
        self.token_expiration = datetime.now() - timedelta(seconds=1)

    @staticmethod
    def check_token(token):
        user = User.query.filter_by(token=token).first()
        if user is None or user.token_expiration < datetime.now():
            return None
        return user
    

    # Post relationship
    posts = relationship('Post', backref='author', lazy='dynamic')

class Post(db.Model):
    
    id = Column(Integer, primary_key=True)  # Change this to primary key
    title = Column(String(80), nullable=False)  # Add a title column
    content = Column(String(255))  # Add a content column for the post
    author_id = Column(Integer, ForeignKey('user.id'))  # Foreign key to User table


class Response:
    def __init__(self, status: str, message: str):
        self.status = status
        self.message = message
    
    def to_dictionary(self):
        return {
            'status': self.status,
            'message': self.message,
        }

class SuccessResponse(Response):
    def __init__(self, message: str = 'Success'):
        super().__init__('sucess', message)

class ErrorResponse(Response):
    def __init__(self, message: str, status_code: int = 400):
        super().__init__('error'. message)
        self.status_code = status_code

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    user = User.query.get(user_id)
    return user


