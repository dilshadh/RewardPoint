from flask import Blueprint

views = Blueprint('views',__name__)

@views.route("/")
def mainPage():
    return "Hi DIlshad welcome to tissdfsdsdf"

@views.route("/home")
def homePage():
    return "this is home page"