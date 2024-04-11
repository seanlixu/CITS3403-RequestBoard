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

@app.route('/login/<username>, <password>', methods=['POST'])
def login():
    # Get data from input
    data = request.json

    # Testing
    
    # data = {'username': 'user6', 'password': 'password9'}
    # user = "user5"
    # password = "pw2"
    user = data.get('username')
    password = data.get('password')

    # cur.execute("SELECT * FROM user")
    # rows = cur.fetchall()
    # for row in rows:
    #     print(row)

    # Error variable for frontend access
    status = ""

    # Check if user or password are empty
    if not user or not password:
        status = "User or Password not found"
        return render_template('login.html', status=status)
        
    
    user = data.get('username')
    password = data.get('password')

    # Select pw where username matches and if nothing return error
    cur.execute("SELECT password FROM user WHERE username=?", (user,))
    # Rename variable. Password tuple. Fetches data of password column
    current_user = cur.fetchone()

    # Check if any results returned
    if not current_user:
        status = "Username or Password not found"
        return render_template('login.html', status=status)
    # Check if hashed password matches input password
    if bcrypt.check_password_hash(current_user[0], password):
        status = "None"
        return redirect('/home')
    else: 
        status = "Incorrect Password, try again"
        return render_template('login.html', status=status)

@app.route('/home')
def render_home():
    return render_template('home.html')

login()


# if __name__ == '__main__':
#     app.run(debug=True)



# from flask import Flask, request, jsonify
# from flask_login import LoginManager
# from flask_bcrypt import Bcrypt
# import sqlite3

# app = Flask(__name__)
# # https://docs.python.org/3/library/sqlite3.html
# # Connect to users.db
# con = sqlite3.connect("users.db")

# # Make connection for executing SQL queries
# cur = con.cursor()

# # Create login manager
# login_manager = LoginManager()

# # Create Bcrypt object with app as param
# bcrypt = Bcrypt(app)
# def valid_user(user, password):
#     # Check if user is empty or password empty
#     if not user or not password:
#         return False, "User or password not found"
    
#     # Select pw where username matches, if nothing return error
#     cur.execute("SELECT password FROM user WHERE username=?", (user,))
#     # Fetch data of password column
#     current_user = cur.fetchone()
#     # Check if results returned
#     if not current_user:
#         return False, "Incorrect username or password"
    
#     if bcrypt.check_password_hash(current_user[0], password):
#         return True, "Login successful"
    
#     else: return False, "Incorrect username or password"

# @app.route('/login', methods=['POST'])
# def login():
#     # Get data from input
#     # data = request.json

#     # Testing
#     data = {'username': 'user5', 'password': 'pw3'}
#     user = "user5"
#     password = "pw2"

#     # Check if user or password are empty
#     if not user or not password:
#         return "User or password not found", 400
    
#     user = data.get('username')
#     password = data.get('password')

#     is_valid, message = valid_user(user, password)

#     if is_valid:
#         return message, 200
    
#     else:
#         return message, 400

        
# # Create function that validates the user and revamp this code.

# # Maybe add more functions like showHomePage and setupAccount


# login()