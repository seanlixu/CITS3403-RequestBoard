from app import app
from flask import render_template
from .login import login
from .register import register_user

@app.route('/login', methods=['POST'])
def login_route():
    return login()

@app.route('/register', methods=['POST'])
def register_route():
    return register_user()

@app.route('/home')
def home():
    return render_template('home.html')