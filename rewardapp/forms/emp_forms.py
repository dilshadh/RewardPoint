from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length 


class LoginForm(FlaskForm):
    username = StringField(validators=[DataRequired(), Length(min=2, max=20)],render_kw={"placeholder": "Username"})
    password = PasswordField(validators=[DataRequired()],render_kw={"placeholder": "Password"})
    remember = BooleanField('Remember Me')
    submit = SubmitField('Log In')