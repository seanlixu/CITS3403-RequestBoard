from app import db
from flask import request, jsonify, redirect, flash, url_for
from flask_login import login_required, current_user
from .forms import PostForm
from .models import Post, User

# Login required to make post
@login_required
def create_post():
    pass
    # Create post form and if valid then add title and content
    form = PostForm()
    if form.validate_on_submit():
        # If no user, then redirect to login
        if current_user is None:
            return redirect(url_for('main.login'))
        # Add new post to Post db using title and content
        new_post = Post(title=form.title, content=form.content, author=current_user)
        db.session.add(new_post)
        db.session.commit()
        # Flash post was posted
        flash(f'{form.title}, Was posted successfully!', 'success')
        # Redirect to post page
        return redirect('/home')
    # Else redirect to posts
    return redirect(url_for('main.userDashboard'), title='Posts', form=form)

# Get all posts
def get_all_posts():
    # Query post db
    posts = Post.query.all()
    post_data = []
    print('getting all posts')
    # If no posts flash message and return empty array
    if not posts:
        flash('No available posts!', 'info')
        return []
    # Else if there are posts, append to posts_data
    elif posts:
        for post in posts:
            post_data.append((post.title, post.content, post.author, post.assigned, post.assigned_user))
            print(post)
        return post_data
    # return empty array if both fail
    else:
        return []



def get_created_jobs(username):
    # Query by username
    user = User.query.filter_by(username=username).first()
    # IF user exists then grab users posts and add to post data
    if user:
        posts = user.posts
        post_data = []
        # If no posts flash message
        if not posts:
            flash(f'User has no uploaded posts!', 'info')
            # Change to redirect for correct page
            return []
        # Else append all post data to post_data and return
        else:
            for post in posts:
                post_data.append((post.title, post.content, post.author, post.assigned, post.assigned_user))
            return post_data
    else:
        return []
   

# Get jobs assigned to user
def get_applied_jobs(username):
    # Query by username
    user = User.query.filter_by(username=username).first()
    # If user exists, get the posts assigned to the user
    if user:
        posts = user.assigned_posts  
        post_data = []
        # If no posts flash message
        if not posts:
            flash(f'User has no assigned posts!', 'info')
            return []  
        # Else append applied job info and return post data
        else:
            for post in posts:
                post_data.append((post.title, post.content, post.author, post.assigned, post.assigned_user))
            return post_data
    else:
        return []

