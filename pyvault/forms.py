from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class LoginForm(FlaskForm):
    email = StringField('Username', validators=[DataRequired(), Email(), Length(min=6, max=120)])
    password = PasswordField('Password', validators = [DataRequired(), Length(min=6, max=120)])
    submit = SubmitField('Sign In')

class RegisterForm(FlaskForm):
    email = StringField('Username', validators=[DataRequired(), Email(), Length(min=6, max=120)])
    password = PasswordField('Password', validators = [DataRequired(), Length(min=6, max=120)])
    confirm = PasswordField('Confirm Password', validators = [DataRequired(), EqualTo('password', message='Las contraseñas deben coincidir.')])

    first_name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=120)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=120)])

    submit = SubmitField('Register')

class AddPasswordForm(FlaskForm):
    service_name = StringField('Service Name', validators=[DataRequired(), Length(min=2, max=120)])
    service_email = StringField('Service Email', validators=[DataRequired(), Length(min=2, max=120)])
    service_password = PasswordField('Password', validators = [DataRequired(), Length(min=2, max=120)])
