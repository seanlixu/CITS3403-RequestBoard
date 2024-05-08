from flask import flash, render_template, redirect, url_for
from flask_login import login_required
from app import flaskApp
from .authentication import handle_register, handle_login, handle_logout


@flaskApp.route("/")
@flaskApp.route("/home")
@flaskApp.route("/index")
@login_required
def home():
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', posts=posts)

@flaskApp.route('/register', methods=['GET', 'POST'])
def register():
    return handle_register()

@flaskApp.route('/login', methods=['GET', 'POST'])
@flaskApp.route('/login/<string:field>', methods=['GET', 'POST'])
def login(field='username'):
    return handle_login(field)

@flaskApp.route('/logout')
def logout():
    return handle_logout()


