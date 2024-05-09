from app import flaskApp, db
from flask import Flask
from flask import request, jsonify, redirect, render_template
from .models import User, SuccessResponse, ErrorResponse
from flask_login import LoginManager, current_user, login_user, logout_user
from werkzeug.security import check_password_hash
from .forms import LoginForm

 

# Create login manager
login_manager = LoginManager()
login_manager.init_app(flaskApp)

# Need secret key for login manager in config.py for now


@flaskApp.route('/login', methods=['POST'])

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

            return redirect('/userDashboard')

        
        else: 
            response = ErrorResponse("Incorrect Password, try again")
            return jsonify(response.to_dictionary), 401
    else:
        # Change to login.html?
        print('form failed')

        print(login_form.errors)
        return render_template('login.html', form=login_form)

