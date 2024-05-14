from flask_login import current_user, login_user, logout_user
from app import  db
from flask import render_template, redirect, flash, url_for, request
from .models import User
from werkzeug.security import generate_password_hash
from .forms import RegisterForm, LoginForm_Username, LoginForm_Email
from urllib.parse import urlsplit


def handle_register():
    print("handle_register")
    if current_user.is_authenticated:
        print("authenticated")
        return redirect(url_for('main.userDashboard'))
    form = RegisterForm()
    if form.validate_on_submit():
        print("validating")
        new_user = User(
            username=form.username.data,
            email=form.email.data,
            password=generate_password_hash(form.password.data)
        )
        db.session.add(new_user)
        db.session.commit()

        flash(f'Account created for {form.username.data}! You can now login', 'success')
        return redirect(url_for('main.login'))
    print("didnt work")
    return render_template('register.html', title='Register', form=form)


def handle_login(field):
    if current_user.is_authenticated:
        return redirect(url_for('main.userDashboard'))
    
    if field == 'email':
        form = LoginForm_Email()
        if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()
            
            # extra server side check to see if user exists
            if not user:
                flash('Email does not exist! Please register or try again', 'danger')
                return redirect(url_for('main.login', field='email'))
            if user and not user.check_password(form.password.data):
                flash('Password is incorrect! Please try again', 'danger')
                return redirect(url_for('main.login', field='email'))
                            
            flash(f'Login successful, welcome {user.username}', 'success')
            login_user(user, remember=form.remember_me.data)
            next_page = request.args.get('next')
            if not next_page or urlsplit(next_page).netloc != '':
                next_page = url_for('main.home')
            return redirect(next_page)
        return render_template('login.html', title='Login', form=form)
    
    elif field == 'username':
        form = LoginForm_Username()
        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first()
            
            # extra server side check to see if user exists
            if not user:
                flash('Username does not exist! Please register or try again', 'danger')
                return redirect(url_for('main.login', field='username'))
            if user and not user.check_password(form.password.data):
                flash('Password is incorrect! Please try again', 'danger')
                return redirect(url_for('main.login', field='username'))
            
            flash(f'Login successful, welcome {user.username}', 'success')
            login_user(user, remember=form.remember_me.data)
            next_page = request.args.get('next')
            if not next_page or urlsplit(next_page).netloc != '':
                next_page = url_for('main.home')
            return redirect(next_page)
        return render_template('login.html', title='Login', form=form)


def handle_logout():
    logout_user()
    flash('You have been logged out', 'info')
    return redirect(url_for('main.home'))