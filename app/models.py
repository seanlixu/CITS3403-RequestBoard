from app import db, login
from datetime import datetime, timezone
from werkzeug.security import check_password_hash
from flask_login import UserMixin


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    # indexing the username and email columns for faster search since will be used for login
    username = db.Column(db.String(64), unique=True, nullable=False, index=True)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    # to store profile picture
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(256), nullable=False)
    # for short bio
    about = db.Column(db.String(256), default='Hello, I am new here!')
    # To know when the account was created for requestee and account page
    account_created = db.Column(db.DateTime, nullable=False, default=datetime.now(timezone.utc))
    ratings = db.Column(db.Float(5.0), default=0.0)
    ratings_count = db.Column(db.Integer(), default=0)
    
    posts = db.relationship('Post', back_populates='author', foreign_keys="[Post.user_id]")
    assigned_posts = db.relationship('Post', back_populates='assigned_user', foreign_keys="[Post.assigned_user_id]")
    
    def __repr__(self):
        return f'<User {self.username}, {self.email}, {self.image_file}>'

    def check_password(self, password):
        return check_password_hash(self.password, password)
    

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.now(timezone.utc), index=True)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    # for the request to be assigned to someone and also to view current jobs
    assigned = db.Column(db.Boolean, default=False)
    assigned_user_id = db.Column(db.Integer, db.ForeignKey('users.id', name='fk_assigned_user_id'), nullable=True, index=True)
    
    author = db.relationship('User', back_populates='posts', foreign_keys=[user_id])
    assigned_user = db.relationship('User', back_populates='assigned_posts', foreign_keys=[assigned_user_id])
    
    def __repr__(self):
        return f'<Post {self.title}, {self.timestamp}>'

    
    