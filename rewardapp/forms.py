from flask_wtf import Form
from wtforms import PasswordField, StringField, HiddenField


class LoginForm(Form):
    userName = StringField('userName')
    password = PasswordField('Password')