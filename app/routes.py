from flask import flash, render_template, redirect, url_for
from flask_login import login_required, current_user
from app.blueprints import main
from .authentication import handle_register, handle_login, handle_logout
from .models import Post
from .posts import get_all_posts, get_applied_jobs, get_created_jobs

@main.route("/")
@main.route("/home")
@main.route("/index")
def home():
    return render_template('index.html', title='Home')

@main.route('/register', methods=['GET', 'POST'])
def register():
    return handle_register()

@main.route('/login', methods=['GET', 'POST'])
@main.route('/login/<string:field>', methods=['GET', 'POST'])
def login(field='username'):
    return handle_login(field)

@main.route('/logout')
def logout():
    return handle_logout()

@main.route('/userDashboard')
@login_required
def userDashboard():
    posts = get_all_posts()
    username = current_user.username
    return render_template('userDashboard.html', posts=posts, username=username)

@main.route('/accepted_jobs')
@login_required
def accepted_jobs(field='username'):
    posts = get_applied_jobs(current_user.username)
    username = current_user.username
    return render_template('userDashboard.html', posts=posts, username=username)


@main.route('/uploaded_jobs')
@login_required
def uploaded_jobs(field='username'):
    posts = get_created_jobs(current_user.username)
    username = current_user.username
    return render_template('userDashboard.html', posts=posts, username=username)

@main.route('/new_job')
@login_required
def new_job():
    posts = get_all_posts()
    username = current_user.username
    return render_template('userDashboard.html', upload=True, username=username)

@main.route('/search')
@login_required
def search_jobs():
    posts = get_all_posts()
    username = current_user.username
    return render_template('userDashboard.html', posts=posts, username=username)