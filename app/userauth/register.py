# Imports
from app import app
from flask import Flask
from flask import request, jsonify, render_template, redirect
from flask_login import Loginmanager
from models import User, SuccessResponse, ErrorResponse
from config import db
from forms import RegisterForm
from werkzeug.security import generate_password_hash

app = Flask(__name__)

@app.route('/register/<username>, <password>', methods=['GET', 'POST'])
def register_user():
# https://www.geeksforgeeks.org/get-the-data-received-in-a-flask-request/
# Check if username and password are not empty, if they are return error
# Check if username taken already
# If not create new user and then add to database
    register_form = RegisterForm()
    if register_form.validate_on_submit():
        user = register_form.username.data
        password = register_form.password.data

    # testing
    # data = {'username': 'user6', 'password': 'password6'}

    # If username and password not empty, return error
    # if user not in data or password not in data:
    #     return()
        if not user or password:
            response = ErrorResponse('Username or password not found')
            return jsonify(response.to_dictionary()), 400

        # Add some password checks, like Must be capital. etc all that.
        if len(user) > 20 or len(password) < 8 or len(password) > 30:
            response = ErrorResponse('User must be less than 20 characters, Password must be between 8 and 30 characters')
            return jsonify(response.to_dictionary()), 400

        # Check if username already taken. Crosscheck with db
        existing_user = User.query.filter_by(username=user).first()
        if existing_user:
            # Change this to error
            response = ErrorResponse('Username is taken, Please choose another')
            return jsonify(response.to_dictionary), 409

            # Hash passwords before insert
        password_hashed = generate_password_hash(password)
        new_user = User(username=user, password_hashed=password_hashed)
        db.session.add(new_user)
        db.session.commit()
            
        response = SuccessResponse('Successful register')
        return redirect('/login')
    return render_template('register.html', form=register_form)
    


