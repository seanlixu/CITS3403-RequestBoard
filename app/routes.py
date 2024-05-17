from flask import flash, render_template, redirect, url_for, request, jsonify
from flask_login import login_required, current_user
from app.blueprints import main
from .authentication import handle_register, handle_login, handle_logout
from .posts import get_all_posts, get_applied_jobs, get_created_jobs
from app import db
from .models import Post, User
from .forms import PostForm

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
def accepted_jobs():
    posts = get_applied_jobs(current_user.username)
    username = current_user.username
    return render_template('userDashboard.html', posts=posts, username=username)

@main.route('/uploaded_jobs')
@login_required
def uploaded_jobs():
    posts = get_created_jobs(current_user.username)
    username = current_user.username
    return render_template('userDashboard.html', posts=posts, username=username)

@main.route('/new_job')
@login_required
def new_job():
    username = current_user.username
    return render_template('userDashboard.html', upload=True, username=username)

@main.route('/search')
@login_required
def search_jobs():
    posts = get_all_posts()
    username = current_user.username
    return render_template('userDashboard.html', posts=posts, username=username)

@main.route('/create_post', methods=['POST'])
@login_required
def create_post():
    data = request.get_json()
    title = data['title']
    content = data['content']
    author_name = data['author']
    assigned = data['assigned']
    assigned_user_name = data['assignedUser']

    # Find the author
    author = User.query.filter_by(username=author_name).first()
    if not author:
        return jsonify({'success': False, 'message': 'Author not found'})

    # Find the assigned user if there is one
    assigned_user = None
    if assigned_user_name:
        assigned_user = User.query.filter_by(username=assigned_user_name).first()
        if not assigned_user:
            return jsonify({'success': False, 'message': 'Assigned user not found'})

    # Create the new post
    new_post = Post(
        title=title,
        content=content,
        author=author,
        assigned=assigned,
        assigned_user=assigned_user
    )

    # Add the new post to the session and commit
    db.session.add(new_post)
    db.session.commit()

    return jsonify({'success': True, 'message': 'Post created successfully'})
