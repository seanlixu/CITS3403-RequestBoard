import flask 
from flask import Flask
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
from wtforms import StringField,  SubmitField, HiddenField
from wtforms.validators import DataRequired, Length, Regexp

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired])
    password = StringField('Password', validators=[DataRequired(), Length(min=8, max=30),  Regexp(r'[A-Za-z0-9]+',message='Password must contain Uppercase, lowercase and a number')])
    csrf_token = HiddenField()
    submit = SubmitField('Login')


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired])
    password = StringField('Password', validators=[DataRequired])
    csrf_token = HiddenField()
    submit = SubmitField('Register')


