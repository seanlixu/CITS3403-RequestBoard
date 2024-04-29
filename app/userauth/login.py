from app import app
from flask import request, render_template, jsonify, redirect
from flask import Flask
from flask_login import LoginManager, current_user
from flask_bcrypt import Bcrypt
from forms import LoginForm
import sqlite3

# Defining success and error response classes
class Response:
    def __init__(self, status: str, message: str):
        self.status = status
        self.message = message
    
    def to_dictionary(self):
        return {
            'status': self.status,
            'message': self.message,
        }

class SuccessResponse(Response):
    def __init__(self, message: str = 'Success'):
        super().__init__('sucess', message)

class ErrorResponse(Response):
    def __init__(self, message: str, status_code: int = 400):
        super().__init__('error'. message)
        self.status_code = status_code


    
app = Flask(__name__)
# Create Bcrypt object with app as param
bcrypt = Bcrypt(app)

# https://docs.python.org/3/library/sqlite3.html
# Connect to users.db
con = sqlite3.connect("users.db")

# Make connection for executing SQL queries
cur = con.cursor()

# Create login manager
login_manager = LoginManager()
login_manager.init_app(app)
# Need secret key for login manager
app.config['SECRET_KEY'] = 'hehe1234567'


login_form = LoginForm()

@app.route('/login/<username>, <password>', methods=['GET', 'POST'])
def login():
    # Get data from input
    
    # logged_in = False
    # user and password variables from forms.py
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = login_form.username.data
        password = login_form.username.data


    # Testing
    # data = {'username': 'user6', 'password': 'password9'}
    # user = "user5"
    # password = "pw2"
    # cur.execute("SELECT * FROM user")
    # rows = cur.fetchall()
    # for row in rows:
    #     print(row)


    # response variable for frontend access
    # Check if user or password are empty
    if not user or not password:
        response = ErrorResponse('Username or Password not found') 
        return jsonify(response.to_dictionary()), 400
        
    
    # Select pw where username matches and if nothing return error
    cur.execute("SELECT password FROM user WHERE username=?", (user,))
    # Rename variable. Password tuple. Fetches data of password column
    current_user = cur.fetchone()

    # Check if any results returned
    if not current_user:
        response = ErrorResponse('No results found')
        return jsonify(response.to_dictionary()), 404
        
    # Check if hashed password matches input password
    if bcrypt.check_password_hash(current_user[0], password):
        response = SuccessResponse('Login successful')
        login_manager(user)
        return redirect('/home')
    else: 
        response = ErrorResponse("Incorrect Password, try again")
        return jsonify(response.to_dictionary), 401
    
    return render_template()
# Create function that checks if user is logged in, implement login manager too for @loginrequired
@login_manager.user_loader
def load_user(user_id):
    return get_user



login()

