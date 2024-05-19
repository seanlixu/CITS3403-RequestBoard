from flask_wtf import FlaskForm
from wtforms import StringField,  SubmitField, PasswordField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Regexp, Email, EqualTo, ValidationError

from app.models import User

pass_min, pass_max = 6, 20
user_min, user_max = 4, 20
class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[
        DataRequired(),
        Length(min=user_min, max=user_max, message=f'Username must be between {user_min} and {user_max} characters long'),
        Regexp(r'^[a-zA-Z0-9_]+$', message='Username must contain only letters, numbers, and underscores')
    ])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[
        DataRequired(),
        Length(min=pass_min, max=pass_max, message=f'Password must be between {pass_min} and {pass_max} characters long'),
        Regexp(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{6,}$', 
            message='Password must contain at least one uppercase letter, one lowercase letter, and one number')
    ])
    confirm_password = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password', message='Passwords must match')])
    submit = SubmitField('Sign Up')
    
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already in use! Please select a different username or Log in')
        
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("Email is already registered! Please use a different email address or Log in")


class LoginForm(FlaskForm):
    password = PasswordField('Password', validators=[
        DataRequired(),
        Length(min=pass_min, max=pass_max, message=f'Password must be between {pass_min} and {pass_max} characters long'),
        Regexp(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{6,}$', 
            message='Password contains at least one uppercase letter, one lowercase letter, and one number')
    ])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
    
class LoginForm_Username(LoginForm):
    username = StringField('Username', validators=[
        DataRequired(),
        Length(min=user_min, max=user_max, message=f'Username is between {user_min} and {user_max} characters long'),
        Regexp(r'^[a-zA-Z0-9_]+$', message='Username contains only letters, numbers, and underscores')
    ])
    
    def validate_username(self, username):
        if self.errors.get('username'):
            return
        user = User.query.filter_by(username=username.data).first()
        if not user:
            raise ValidationError('Username does not exist! Please register or try again')
        
    def validate_password(self, password):
        if self.errors.get('password'):
            return
        user = User.query.filter_by(username=self.username.data).first()
        if user and not user.check_password(password.data):
            raise ValidationError('Password is incorrect! Please try again')
        
class LoginForm_Email(LoginForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    
    def validate_email(self, email):
        if self.errors.get('email'):
            return
        user = User.query.filter_by(email=email.data).first()
        if not user:
            raise ValidationError('Email does not exist! Please register or try again')
        
    def validate_password(self, password):
        if self.errors.get('password'):
            return
        user = User.query.filter_by(email=self.email.data).first()
        if user and not user.check_password(password.data):
            raise ValidationError('Password is incorrect! Please try again')
        
        
title_min, title_max = 6, 30   
content_min, content_max = 20, 300
class PostForm(FlaskForm):
    title = StringField("Title", validators=[
        DataRequired(),
        Length(min=title_min, max=title_max, message=f'Title must be between {title_min} and {title_max} characters long')
    ])
    content = TextAreaField("Content", validators=[
        DataRequired(),
        Length(min=content_min, max=content_max, message=f'Content must be between {content_min} and {content_max} characters long')
    ])
    submit = SubmitField('Create Post')

    # Add error checkers