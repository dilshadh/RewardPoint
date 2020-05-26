from rewardapp import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from rewardapp import login_manager
@login_manager.user_loader
def load_employee(e_id):
    return Employee.query.get(int(e_id))

class Employee(db.Model, UserMixin):
    e_id = db.Column(db.Integer, primary_key=True)
    e_username = db.Column(db.String(80), unique=True)
    e_password_hash = db.Column(db.String(128))
    e_name = db.Column(db.String(80))
    e_phone_number = db.Column(db.String(80), unique=True)
    
    def __init__(self, e_username, e_name, e_phone_number):
        self.e_username = e_username
        self.e_name = e_name
        self.e_phone_number = e_phone_number

    def set_password(self, password):
        self.e_password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.e_password_hash, password)
    
    def get_id(self):
           return (self.e_id)

class Customer(db.Model, UserMixin):
    c_id = db.Column(db.Integer, primary_key=True)
    c_username = db.Column(db.String(80), unique=True)
    c_name = db.Column(db.String(80))
    c_phone_number = db.Column(db.String(80), unique=True)
    c_email = db.Column(db.String(80), unique=True)

    def __init__(self, c_username, c_name, c_phone_number, c_email):
        self.c_username = c_username
        self.c_name = c_name
        self.c_phone_number = c_phone_number
        self.c_email = c_email

    def get_id(self):
           return (self.c_id)