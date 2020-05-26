from flask_wtf import Form, FlaskForm
from wtforms import PasswordField, StringField, HiddenField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
import phonenumbers
from rewardapp.model import Employee

class LoginForm(FlaskForm):
    username = StringField('Username', 
                            validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password',
                            validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Log In')

class EmployeeRegForm(FlaskForm):

    empName = StringField('Employee Name',

                            validators=[DataRequired(), Length(min=2, max=20)])

    userName = StringField('User Name',

                            validators=[DataRequired(), Length(min=2, max=20)])

    phonenumber = StringField('Phone Number',

                        validators=[DataRequired()])

    password = PasswordField('Password', validators=[DataRequired()])
    

    confirm_password = PasswordField('Confirm Password',

                                        validators=[DataRequired(), EqualTo('password')])

    submit = SubmitField('Submit')

    def validate_phonenumber(self, phonenumber):
        if Employee.query.filter_by(e_phone_number=phonenumber.data).first():
            raise ValidationError('Phone number already registered.') 
        try:
            val = int(phonenumber.data)
            if len(phonenumber.data) > 10:
                raise ValidationError('Invalid phone number!')
            
            
        except:
                raise ValidationError('Invalid phone number!')
    def validate_userName(self, userName):
        if Employee.query.filter_by(e_username=userName.data).first():
            raise ValidationError('User name already exist.')       