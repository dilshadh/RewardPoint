from flask import Blueprint, render_template, request, flash
from flask_login import login_required
from rewardapp.forms.e_loginForm import LoginForm
from rewardapp.model import Customer, Employee
from rewardapp import db
views = Blueprint('views', __name__, template_folder="templates")

@views.route("/", methods=['GET'])
def mainPage():
    return render_template("base.html")

@views.route("/customerRegistration", methods=['GET','POST'])
@login_required
def CustomerRegistration():
    if request.method == 'GET':
        return render_template('customerRegistration.html')
    c_username =  request.form.get('username')
    c_fullname = request.form.get('fullname')
    c_phone_number = request.form.get('phonenumber')
    c_email = request.form.get('email')
    customer = Customer.query.filter_by(c_username=c_username).first()
    if customer:
        flash('Customer Already Exists!')
        return render_template('customerRegistration.html')
    customer = Customer(c_username=c_username,c_name=c_fullname,c_phone_number=c_phone_number,c_email=c_email)
    db.session.add(customer)
    db.session.commit()
    flash('Customer Added Successfully!')
    return render_template("customerRegistration.html")