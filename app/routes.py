from flask import Flask, render_template, redirect
from .register import register_user
# from .login import login, logout_user
from .models import ErrorResponse, SuccessResponse, User
from flask_login import LoginManager
from app import flaskApp, db
from app import flaskApp, db
from .forms import RegisterForm
from werkzeug.security import generate_password_hash


from flask import request, jsonify, redirect, render_template

from flask_login import LoginManager, current_user, login_user, logout_user
from werkzeug.security import check_password_hash
from .forms import LoginForm


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
        return redirect('/login')
    else:
        print('form valid failed')
        print(" >> "    + str(register_form.errors))
        return render_template('/register.html', form=register_form)

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


@flaskApp.route('/logout', methods=['GET', 'POST'])
def logout_route():
    logout_user()
    return redirect('/home')



