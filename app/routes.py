from flask import render_template, request
from flask_login import login_required, current_user
from app.blueprints import main
from .authentication import handle_register, handle_login, handle_logout
from .forms import PostForm
from .posts import get_all_posts, get_applied_jobs, get_created_jobs, create_post, assign, get_available_jobs


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
@login_required
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

@main.route('/new_job', methods=['GET', 'POST'])
@login_required
def new_job():
    create_post()
    form = PostForm()
    username = current_user.username
    return render_template('userDashboard.html', form=form, upload=True, username=username)


@main.route('/search')
@login_required
def search_jobs():
    posts = get_available_jobs()
    username = current_user.username
    return render_template('userDashboard.html', posts=posts, username=username)

@main.route('/assign', methods=['GET', 'POST'])
@login_required
def assign_job():
    post_id = request.form.get('post_id')
    username = current_user.username
    assign(post_id)
    posts = get_applied_jobs(current_user.username)
    return render_template('userDashboard.html', posts=posts, username=username)
