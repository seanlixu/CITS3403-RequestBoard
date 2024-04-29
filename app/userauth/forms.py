import flask 
from flask import Flask
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
from wtforms import IntegerField, StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired])
    password = StringField('Password', validators=[DataRequired])
    submit = SubmitField('Login')


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired])
    password = StringField('Password', validators=[DataRequired])
    submit = SubmitField('Register')


