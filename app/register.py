# Imports
from app import flaskApp, db
from flask import Flask
from flask import request, jsonify, render_template, redirect
from .models import User, SuccessResponse, ErrorResponse
# from app import flaskApp, db
from .forms import RegisterForm
from werkzeug.security import generate_password_hash


@flaskApp.route('/register', methods=['GET', 'POST'])
def register_user():
# https://www.geeksforgeeks.org/get-the-data-received-in-a-flask-request/
# Check if username and password are not empty, if they are return error
# Check if username taken already
# If not create new user and then add to database
    print('registering')
    register_form = RegisterForm()
    if register_form.validate_on_submit():
        print('inside')
        user = register_form.username.data
        password = register_form.password.data

    # testing
    # data = {'username': 'user6', 'password': 'password6'}
    # print(user)
        # print(password)
    # If username and password not empty, return error
    # if user not in data or password not in data:
    #     return()
   
        if len(user) <= 0 or len(password) <= 0:
            # message = 'User or pw not found'
            response = ErrorResponse('Username or password not found')
            return jsonify(response.to_dictionary()), 400

        # Add some password checks, like Must be capital. etc all that.
        if len(user) > 20 or len(password) < 8 or len(password) > 30:
            response = ErrorResponse('User must be less than 20 characters, Password must be between 8 and 30 characters')
            # print("check 1 worked")
            return jsonify(response.to_dictionary()), 400

        # Check if username already taken. Crosscheck with db
        existing_user = db.session.query(User).filter_by(username=user).first()
        if existing_user:
            # Change this to error
            response = ErrorResponse('Username is taken, Please choose another')
            return jsonify(response.to_dictionary()), 409

            # Hash passwords before insert
        password_hashed = generate_password_hash(password)
        new_user = User(username=user, password=password_hashed)
        db.session.add(new_user)
        db.session.commit()
        # print('finished')
        response = SuccessResponse('Successful register')
        # Sean change to login.html
        return redirect('/home')
    else:
        # change to register.html or whatever.html when register fails.
        print('form valid failed')
        return render_template('/register.html', form=register_form)
    


