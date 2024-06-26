from app import db
from flask import request, flash, render_template
from flask_login import login_required, current_user
from .forms import PostForm
from .models import Post, User

# Login required to make post
@login_required
def create_post():
    print('Posting')
    # Create post form and if valid then add title and content
    username = current_user.username
    form = PostForm()
    # print(username)
    # print(form.title.data)
    # print(form.content.data)
    if request.method == 'POST':
        if form.validate_on_submit():
            # print("Form validated")
            # Add new post to Post db using title and content
            new_post = Post(
                title=form.title.data,
                content=form.content.data,
                author=current_user
            )
            
            db.session.add(new_post)
            db.session.commit()
            # Flash post was posted
            flash(f'Job {form.title.data} was posted successfully!', 'success')
            # Redirect to post page
            return render_template('userDashboard.html', username=username)
        else:
            print(form.errors)
            flash(f"Form invalid, Please try!", "error")
            return render_template('userDashboard.html', username=username)
    # Else redirect to posts
    return render_template('userDashboard.html', username=username)

def get_available_jobs():
    posts = Post.query.all()
    post_data = []
    # if not post, then if not assigned
     # for post in post loop then append data then return it 
    if not posts:
        flash('No available jobs!', 'info')
        return []
    elif posts:
        for post in posts:
            if post.assigned != True:
                post_data.append((post.title, post.id, post.content, post.author, post.assigned, post.assigned_user))
        return post_data
    
    # if fail return nothing
    else: 
        return[]
    


    pass
# Get all posts
def get_all_posts():
    # Query post db
    posts = Post.query.all()
    post_data = []
    # print('getting all posts')
    # If no posts flash message and return empty array
    if not posts:
        flash('No available jobs!', 'info')
        return []
    # Else if there are posts, append to posts_data
    elif posts:
        for post in posts:
            post_data.append((post.title, post.id, post.content, post.author, post.assigned, post.assigned_user))
            print(post.id)
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
            flash(f'You have not posted any jobs!', 'info')
            # Change to redirect for correct page
            return []
        # Else append all post data to post_data and return
        else:
            for post in posts:
                post_data.append((post.title, post.id, post.content, post.author, post.assigned, post.assigned_user))
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
            flash(f'You have not accepted any jobs!', 'info')
            return []  
        # Else append applied job info and return post data
        else:
            for post in posts:
                post_data.append((post.title, post.id, post.content, post.author, post.assigned, post.assigned_user))
            return post_data
    else:
        return []


def assign(post_id):
    username = current_user.username
    post_id = request.form.get('post_id')
    post = Post.query.get(post_id)
    
    if post:
        if post.assigned:
            flash('Post already assigned!', 'danger')
            return
        if post.author.username == username:
            flash('You cannot assign the post to yourself as you are the author!', 'danger')
            return
         
        post.assigned = True
        post.assigned_user_id = current_user.id
        db.session.commit()
        flash('Post assigned successfully!', 'success')
    else:
        flash('Post not found!', 'error')