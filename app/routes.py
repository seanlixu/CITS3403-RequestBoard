from flask import Flask, render_template, redirect
from .register import register_user
from .models import ErrorResponse, SuccessResponse, User
from app import flaskApp, db


@flaskApp.route("/")
def home():
    return render_template("test.html")

@flaskApp.route('/login', methods=['GET', 'POST'])
def test_login():
    # return "<p> logged in </p>"
    return render_template("test.html")

@flaskApp.route('/register', methods=['GET', 'POST'])
def register_route():
    return register_user()

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