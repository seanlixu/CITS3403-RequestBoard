from app import app
from flask import request, render_template, jsonify, redirect
from flask import Flask
from models import User, SuccessResponse, ErrorResponse
from flask_login import LoginManager, current_user, login_user, logout_user
from werkzeug.security import check_password_hash
from forms import LoginForm


 
app = Flask(__name__)



# Create login manager
login_manager = LoginManager()
login_manager.init_app(app)

# Need secret key for login manager
app.config['SECRET_KEY'] = 'hehe1234567'


login_form = LoginForm()

@app.route('/login/<username>, <password>', methods=['GET', 'POST'])
def login():

    # logged_in = False
    # user and password variables from forms.py
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = login_form.username.data
        password = login_form.password.data


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

        user = User.query.filter_by(user=user).first()

        # Check if any results returned
        if not user:
            response = ErrorResponse('No user with that name found')
            return jsonify(response.to_dictionary()), 404
            
        # Check if hashed password matches input password
        if check_password_hash(user.password_hashed, password):
            login_user(user)
            response = SuccessResponse('Login successful')
            return redirect('/home')
        
        else: 
            response = ErrorResponse("Incorrect Password, try again")
            return jsonify(response.to_dictionary), 401
    return redirect('/login')   

def logout():
    logout_user()
    return redirect("/login")