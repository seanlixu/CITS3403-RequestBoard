from app import flaskApp, db
from flask import request, jsonify,redirect
from flask_login import login_required, current_user
from .forms import PostForm
from .models import Post


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