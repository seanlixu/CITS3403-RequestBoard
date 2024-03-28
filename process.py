from flask import Flask, request
import sqlite3
app = Flask(__name__)
# https://docs.python.org/3/library/sqlite3.html
# Connect to users.db
con = sqlite3.connect("users.db")
# Make connection for executing SQL queries
cur = con.cursor()
# Create database
cur.execute("CREATE TABLE user(id INTEGER PRIMARY KEY, username , password)")

@app.route('/register', methods=['GET', 'POST'])
def register_user():
# https://www.geeksforgeeks.org/get-the-data-received-in-a-flask-request/
# Check if username and password are not empty, if they are return error
# Check if username taken already
# If not create new user and then add to database
    data = request.json
    user = data.get('username')
    password = data.get('password')
    def check_registration(username, password):
        if user not in data or password not in data:
            return()
        if user.length <= 0 or password.length <= 0:
            return()
        
        # Check if username already taken. Crosscheck with db
        cur.execute("SELECT username FROM user WHERE username=", (username,))
        row = cur.fetchone()
        # Return result
    check_registration(user, password)



    


# Check if username and password are not empty, if they are return error
# Check if username taken already
# If not create new user and then add to database

# Receive data
# Validate data
# Create user new data
#  Store user in database
#  
@app.route('login', methods=['POST'])
def login():
# Use SQL and select user and pw, if not user, return error
    
    pass
    # can use request.json and request.form
