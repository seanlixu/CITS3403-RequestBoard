from flask import Flask
from flask import request, render_template, jsonify, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app import db
# User model
class User(db.Model):
    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    password = Column(String(128), nullable=False)
    rating = Column(Float(5.0), default=0.0)
    ratings_count = Column(Integer(), default=0)

    # Post relationship
    posts = relationship('Post', backref='author', lazy='dynamic')

class Post(db.Model):
    
    id = Column(Integer, primary_key=True)  # Change this to primary key
    title = Column(String(80), nullable=False)  # Add a title column
    content = Column(String(255))  # Add a content column for the post
    author_id = Column(Integer, ForeignKey('user.id'))  # Foreign key to User table
# class User:
#     def __init__(self, id, username, password):
#         self.id = id
#         self.username = username
#         self.password = password


# Testing for paul
# user = User(username="admin")
# post1 = user.posts(title='hey', content='fiorst post', author=user)

# user.posts.append(post1)