from app import app
import sqlite3
from flask import request, render_template, jsonify
from .login import login
from .register import register_user

# Login route
@app.route('/login', methods=['POST'])
def login_route():
    return login()

# Register route
@app.route('/register', methods=['POST'])
def register_route():
    return register_user()

# Home route
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/user/<username>')
def get_user(username):
    pass