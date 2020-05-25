from flask import Blueprint, render_template, request
from rewardapp.forms import LoginForm
views = Blueprint('views', __name__, template_folder="templates")

@views.route("/")
def mainPage():
    return render_template("base.html")

