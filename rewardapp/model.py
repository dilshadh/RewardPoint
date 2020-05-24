from rewardapp import db
from werkzeug.security import generate_password_hash, check_password_hash

class Employee(db.Model):
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