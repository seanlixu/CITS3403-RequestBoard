from app import db, login
from datetime import datetime, timezone
from werkzeug.security import check_password_hash
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    # indexing the username and email columns for faster search since will be used for login
    username = db.Column(db.String(64), unique=True, nullable=False, index=True)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    # to store profile picture
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(256), nullable=False)
    ratings = db.Column(db.Float(5.0), default=0.0)
    ratings_count = db.Column(db.Integer(), default=0)
    
    posts = db.relationship('Post', back_populates='author')
    # posts = db.relationship('Post', back_populates='author', lazy='dynamic')
    
    def __repr__(self):
        return f'<User {self.username}, {self.email}, {self.image_file}>'

    def check_password(self, password):
        return check_password_hash(self.password, password)
    
@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.now(timezone.utc), index=True)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    
    author = db.relationship('User', back_populates='posts')
    # author = db.relationship('User', back_populates='posts', lazy='dynamic')
    def __repr__(self):
        return f'<Post {self.title}, {self.timestamp}>'

    
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
        super().__init__('success', message)

class ErrorResponse(Response):
    def __init__(self, message: str = 'Error'):
        super().__init__('error', message)
    
        