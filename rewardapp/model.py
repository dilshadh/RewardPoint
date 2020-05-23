from rewardapp import db
class UserDilshad(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    onemo = db.Column(db.String(120), unique=True)
    def __init__(self, username, email, onemo):
        self.username = username
        self.email = email
        self.onemo = onemo

