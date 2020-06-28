from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, BooleanField, IntegerField, TextField
from wtforms.validators import DataRequired, Length, ValidationError
from rewardapp.model import Customer
import phonenumbers
from email_validator import validate_email, EmailNotValidError

class CustomerRegistrationForm(FlaskForm):
    username = StringField('Username', 
                            validators=[DataRequired(), Length(min=2, max=20)])
    fullname = StringField('Full Name', 
                            validators=[DataRequired(), Length(min=2, max=20)])
    phonenumber = StringField('Phone', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_phonenumber(self, phonenumber):
        if Customer.query.filter_by(c_phone_number=phonenumber.data).first():
            raise ValidationError('Phone number already registered.') 
        try:
            val = int(phonenumber.data)
            if len(phonenumber.data) > 10:
                raise ValidationError('Invalid phone number!')
            
        except:
                raise ValidationError('Invalid phone number!')

    def validate_email(self, email):
        if Customer.query.filter_by(c_email=email.data).first():
            raise ValidationError('Email already registered!') 
        try:
            valid = validate_email(email.data)
            email = valid.email
        except EmailNotValidError as e:
            raise ValidationError('Invalid Email.Please check again!') 

class SearchCustomerForm(FlaskForm):
    phonenumber = StringField('Phone Number', id='phone_autocomplete', render_kw={"placeholder": "Customer Phone Number"}
                       ,validators=[DataRequired()])
    fullname = StringField('Full Name', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired()])
    submit = SubmitField('Submit')
    deleteCustomer = SubmitField('Remove Customer')