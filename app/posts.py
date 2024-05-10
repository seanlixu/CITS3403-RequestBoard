from app import flaskApp, db
from flask import request, jsonify, redirect, flash, url_for
from flask_login import login_required, current_user
from .forms import PostForm
from .models import Post, User


@login_required
@flaskApp.route('/create', methods=['GET', 'POST'])
def create_post():
    print('create post')
    create_form = PostForm()
    if create_form.validate_on_submit():
        title = create_form.title.data
        content = create_form.content.data

        if current_user is None:
            return redirect('/login')

        new_post = Post(title=title, content=content, author=current_user)
        db.session.add(new_post)
        db.session.commit()

        return redirect('/home')
    
    return redirect('/login')

@flaskApp.route('/display', methods=['GET'])
def get_all_posts():
    posts = Post.query.all()
    post_data = []

    for post in posts:
        data = {
            'title': post.title,
            'content': post.content
        }
        post_data.append(data)
    return jsonify(post_data)


def get_created_jobs(username):
    user = User.query.filter_by(username=username).first()
    if user:
        user_posts = user.posts
        post_data = []

        for post in user_posts:
            data = [post.title, post.content]
        post_data.append(data)
        return jsonify(post_data)
    else:
        flash("User not found")
        # create posts route
        return redirect(url_for(''))
    
def get_applied_jobs(username):
    user  = User.query.filter_by(username=username).first()
    if user:
        applied_posts = user.assigned_posts.all()
        post_data = []
        for post in applied_posts:
            data = [post.title, post.content]
        post_data.append(data)
    return jsonify(post_data)