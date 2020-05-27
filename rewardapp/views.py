from flask import Blueprint, render_template, request, flash
from flask_login import login_required
from rewardapp.forms.cust_forms import CustomerRegistrationForm
from rewardapp.model import Customer, Employee
from rewardapp import db
views = Blueprint('views', __name__, template_folder="templates")

@views.route("/", methods=['GET'])
def mainPage():
    return render_template("base.html")

@views.route("/home", methods=['GET'])
def homePage():
    return render_template("homePage.html")

@views.route("/customerRegistration", methods=['GET','POST'])
@login_required
def CustomerRegistration():
    form = CustomerRegistrationForm()
    if form.validate_on_submit():
        c_username =  form.username.data
        c_fullname = form.fullname.data
        c_phone_number = form.phonenumber.data
        c_email = form.email.data
        customer = Customer.query.filter_by(c_username=c_username).first()
        if customer:
            flash('Username Already Exists!','danger')
            return render_template('customerRegistration.html',title='Customer Registration', form=form)
        customer = Customer(c_username=c_username,c_name=c_fullname,c_phone_number=c_phone_number,c_email=c_email)
        db.session.add(customer)
        db.session.commit()
        flash('Customer Added Successfully!','success')
    return render_template("customerRegistration.html",title='Customer Registration', form=form)