from app import app
from flask import request, jsonify, render_template, flask_bcrypt
# from flask_login import Loginmanager
from flask_bcrypt import Bcrypt
import sqlite3


app = Flask(__name__)
# https://docs.python.org/3/library/sqlite3.html
# Connect to users.db
con = sqlite3.connect("users.db")

# Make connection for executing SQL queries
cur = con.cursor()


# Create Bcrypt object with app as param
bcrypt = Bcrypt(app)

# Create database
try:
    cur.execute("CREATE TABLE user(id INTEGER PRIMARY KEY, username , password)")
except sqlite3.OperationalError:
    pass    

@app.route('/register/<username>, <password>', methods=['GET', 'POST'])
def register_user():
# https://www.geeksforgeeks.org/get-the-data-received-in-a-flask-request/
# Check if username and password are not empty, if they are return error
# Check if username taken already
# If not create new user and then add to database
    # data = request.json

    # testing
    data = {'username': 'user6', 'password': 'password6'}
    
    user = data.get('username')
    password = data.get('password')


    # Set status variable to return to frontend
    status = ''
    # user = request.form.get('username')
    # password = request.form.get('password')

    # If username and password not empty, return error
    # if user not in data or password not in data:
    #     return()
    if not user or not password:
        status = 'User or password not found'
        return render_template('signUp.html')
    
    # Add some password checks, like Must be capital. etc all that.
    if len(user) > 20 or len(password) < 8 or len(password) > 30:
        status = 'User must be less than 20 characters, Password must be between 8 and 30 characters'
        return render_template('signUp.html')
    

    # Check if username already taken. Crosscheck with db
    cur.execute("SELECT username FROM user WHERE username=?", (user,))
    existing_user = cur.fetchone()

    if existing_user:
        # Change this to error
        status = 'User already exists, try again'
        return render_template('signUp.html')
        
    else:
        # Hash passwords before insert
        password_hashed = bcrypt.generate_password_hash(password)
        # Insert into database after check is done
        cur.execute("INSERT INTO user (username, password) VALUES (?, ?)", (user, password_hashed))
        con.commit()
        
        status = 'Account created'
        return render_template('/home')

@app.route('/home')
def home():
    return render_template('home.html')
    # Printing users / For testing
    # cur.execute("SELECT * FROM user")
    # rows = cur.fetchall()
    # for row in rows:
    #     print(row)


    


register_user()
    


