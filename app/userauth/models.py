import flask
from flask import request, render_template, jsonify, redirect
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from .__init__ import db
# Database model
class User(db.Model):
    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    password = Column(String(128), nullable=False)
    rating = Column(Float(5.0), default=0.0)
    ratings_count = Column(Integer(), default=0)
    # Post relationship
    posts = relationship('Post', backref='author', lazy='dynamic')
