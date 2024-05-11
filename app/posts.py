from app import flaskApp, db
from flask import request, jsonify, redirect, flash, url_for
from flask_login import login_required, current_user
from .forms import PostForm
from .models import Post, User

# Login required to make post
@login_required
def create_post():
    # Create post form and if valid then add title and content
    form = PostForm()
    if form.validate_on_submit():
        # If no user, then redirect to login
        if current_user is None:
            return redirect(url_for('/login'))
        # Add new post to Post db using title and content
        new_post = Post(title=form.title, content=form.content, author=current_user)
        db.session.add(new_post)
        db.session.commit()
        # Flash post was posted
        flash(f'{form.title}, Was posted successfully!', 'success')
        # Redirect to post page
        return redirect('/home')
    # Else redirect to posts
    return redirect('/posts', title='Posts', form=form)

# Get all posts
def get_all_posts():
    # Query post db
    posts = Post.query.all()
    post_data = []
    #  For each post get title and content and append to post_data
    for post in posts:
        data = [post.title, post.content]
        post_data.append(data)
    # Maybe add flash for all posts grabbed
    return jsonify(post_data)

def get_created_jobs(username):
    # Query user by username
    user = User.query.filter_by(username=username).first()
    # IF user exists then grab users posts and add to post data
    if user:
        posts = user.posts
        post_data = []
        for post in posts:
            data = [post.title, post.content]
            post_data.append(data)
        return jsonify(post_data)
    else:
        flash(f'User was not found, Please try again!', 'error')
        # Change to redirect for correct page
        return redirect(url_for(''))

# Get jobs assigned to user
def get_applied_jobs(username):

    # Query by username
    user  = User.query.filter_by(username=username).first()
    # If user exists then add posts assigned to user to data and return as json
    if user:
        posts = user.assigned_posts.all()
        post_data = []
        for post in posts:
            data = [post.title, post.content]
            post_data.append(data)
        return jsonify(post_data)
    else:
        flash(f'User has no assigned posts', 'info')
        # change to correct page
        return redirect(url_for('home'))
    