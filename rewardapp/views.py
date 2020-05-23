from flask import Blueprint
from rewardapp import db
views = Blueprint('views',__name__)

@views.route("/")
def mainPage():
    return "Hi DIlshad welcome to tissdfsdsdf"

@views.route("/home")
def homePage():
    db.create_all()
    return "this is home page"