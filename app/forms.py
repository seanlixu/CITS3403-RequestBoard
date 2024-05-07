from flask import Flask
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
from wtforms import StringField,  SubmitField, HiddenField, PasswordField
from wtforms.validators import DataRequired, Length, Regexp

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired()])
    csrf_token = HiddenField()
    submit = SubmitField('Login')

    class Meta:
        # Disable client-side validation temporarily
        csrf = False

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired()])
    csrf_token = HiddenField()
    submit = SubmitField('Register')

    # username = StringField('Username', validators=[DataRequired()], id='new-username')
    # password = PasswordField('Password', validators=[DataRequired()], id='new-password')
    # confirm_password = PasswordField('Confirm Password', validators=[DataRequired()], id='confirm-password')
    # submit = SubmitField('Register')
    # username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
    # password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=30)])

    class Meta:
        # Disable client-side validation temporarily
        csrf = False
