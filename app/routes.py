from flask import Flask, render_template, redirect
from .register import register_user
from .login import login, logout_user
from .models import ErrorResponse, SuccessResponse, User
from flask_login import LoginManager
from app import flaskApp, db

# Login manager
login_manager = LoginManager()
login_manager.init_app(flaskApp)

@login_manager.user_loader
def load_user(user_id):
    user = User.query.get(user_id)
    return user

@flaskApp.route("/")
@flaskApp.route("/home")
def home():
    return render_template("test.html")

@flaskApp.route('/login', methods=['GET', 'POST'])
def login_route():
    # return "<p> logged in </p>"
    return login()

@flaskApp.route('/logout', methods=['GET', 'POST'])
def logout_route():
    logout_user()
    return redirect('/home')

@flaskApp.route('/register', methods=['GET', 'POST'])
def register_route():
    return register_user()
