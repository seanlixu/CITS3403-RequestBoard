from app import app
from flask import request, render_template, jsonify, redirect
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
import sqlite3

app = Flask(__name__)
# https://docs.python.org/3/library/sqlite3.html
# Connect to users.db
con = sqlite3.connect("users.db")

# Make connection for executing SQL queries
cur = con.cursor()

# Create login manager
login_manager = LoginManager()

# Create Bcrypt object with app as param
bcrypt = Bcrypt(app)

@app.route('/login/<username>, <password>', methods=['GET', 'POST'])
def login():
    # Get data from input
    data = request.json

    # Testing
    
    # data = {'username': 'user6', 'password': 'password9'}
    # user = "user5"
    # password = "pw2"
    # cur.execute("SELECT * FROM user")
    # rows = cur.fetchall()
    # for row in rows:
    #     print(row)


    # User and password variables from data
    user = data.get('username')
    password = data.get('password')

    # response variable for frontend access
    response = {'status': '', 'message': ''}
    # Check if user or password are empty
    if not user or not password:
        response['status'] = 'error'
        response['message'] = "Username or password not found"
        return jsonify(response), 400
        
        
    
    # Select pw where username matches and if nothing return error
    cur.execute("SELECT password FROM user WHERE username=?", (user,))
    # Rename variable. Password tuple. Fetches data of password column
    current_user = cur.fetchone()

    # Check if any results returned
    if not current_user:
        response['status'] = 'error'
        response['message'] = "Username or Password not found"
        return jsonify({'status': 'error', 'message': status}), 404
        
    # Check if hashed password matches input password
    if bcrypt.check_password_hash(current_user[0], password):
        response['status'] = 'success'
        response['message'] = "Login successful"
        return redirect('/home')
    else: 
        status = "Incorrect Password, try again"
        response['status'] = 'error'
        response['message'] = "Incorrect Password, try again"
        return jsonify(response), 401
        
login()

