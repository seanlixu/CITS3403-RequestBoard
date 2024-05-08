from flask import Flask, render_template, redirect
from .register import register_user
from .models import ErrorResponse, SuccessResponse, User
from app import flaskApp, db
from app import flaskApp, db

from flask import request, jsonify, redirect, render_template

from flask_login import LoginManager, current_user, login_user, logout_user
from werkzeug.security import check_password_hash
from .forms import LoginForm



@flaskApp.route("/")
def home():
    return render_template("register.html")

@flaskApp.route('/login', methods=['GET', 'POST'])
def login():
    # user and password variables from forms.py
    print('logging in')
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = login_form.username.data
        password = login_form.password.data


        # response variable for frontend access
        # Check if user or password are empty
        if len(user) <= 0 or len(password) <= 0:
            response = ErrorResponse('Username or Password not found') 
            return jsonify(response.to_dictionary()), 400

        user = User.query.filter_by(username=user).first()

        # Check if any results returned
        if not user:
            response = ErrorResponse('No user with that name found')
            return jsonify(response.to_dictionary()), 404
            
        # Check if hashed password matches input password
        if check_password_hash(user.password, password):

            login_user(user)
            response = SuccessResponse('Login successful')
            # print('check pw worked')
            # Change to home page .html
            return redirect('/userdashboard')
        
        else: 
            response = ErrorResponse("Incorrect Password, try again")
            return jsonify(response.to_dictionary), 401
    else:
        # Change to login.html?
        print('form failed')
        print(login_form.errors)
        return render_template('login.html', form=login_form)

@flaskApp.route('/register', methods=['GET', 'POST'])
def register():
    return render_template("register.html")

@flaskApp.route("/userdashboard")
def userDashboard():
    return render_template("userDashboard.html")

@flaskApp.route("/profile")
def profile():
    return render_template("profile.html")


# @flaskApp.route('/register', methods=['GET', 'POST'])
# def test_register():
#     # users = db.session.query('users.db').all()  # Query all users
#     # for user in users:
#     #     print(user.username)
#     response = register_user()
    
#     # Handle successful or error response from register_user
#     if isinstance(response, ErrorResponse):  # Check for error response
#         # Display error message to the user (e.g., render a template)
#         return render_template('register.html', error_message=response.message)
#     else:
#         # Handle successful registration (e.g., redirect to login page)
#         return redirect('/login')

    # return render_template('register.html')  # Placeholder for GET request