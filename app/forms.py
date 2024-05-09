from flask import Flask
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
from wtforms import StringField,  SubmitField, HiddenField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Length, Regexp

class MyBaseForm(FlaskForm):
    class Meta:
        csrf = True
        crsf_secret = "not-very-secret"
# Login form
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired()])
    csrf_token = HiddenField()
    submit = SubmitField('Login')
    

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired()], )
    csrf_token = HiddenField()
    submit = SubmitField('Register')

# class PostForm(FlaskForm):
#     title = StringField('Title', validators=[DataRequired()])
#     content = TextAreaField('Content', validators=[DataRequired()])
#     submit = SubmitField('Create Post')
