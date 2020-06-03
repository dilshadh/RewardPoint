from flask import Blueprint, render_template, request, flash, jsonify, Response, redirect, url_for
from flask_login import login_required
from rewardapp.forms.cust_forms import CustomerRegistrationForm, SearchCustomerForm
from rewardapp.model import Customer, Employee
from rewardapp import db
import json
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

@views.route('/autocomplete', methods=['GET'])
@login_required
def autocomplete():
    results = []
    search = request.args.get('term')
    query = Customer.query.filter(Customer.c_phone_number.like('%' + str(search) + '%')).all()
    for customer in query:
        customerObj = customer.__dict__
        del customerObj['_sa_instance_state']
        results.append(customerObj)
    return jsonify(results)

@views.route("/searchCustomer", methods=['GET', 'POST'])
@login_required
def searchCustomer():
    form = SearchCustomerForm()
    if form.validate_on_submit():
        print(form)
        if form.submit.data:
            pass
        elif form.deleteCustomer:
            phonenumber = form.phonenumber.data
            customer = Customer.query.filter_by(c_phone_number=phonenumber).first()
            if customer:
                db.session.delete(customer)
                db.session.commit()
                flash('Customer Removed Successfully','success')
            else:
                flash('Customer Not Found','danger')
            return jsonify(dict(redirect=url_for('views.searchCustomer')))
    return render_template("searchCustomer.html",title='Customer Search',form=form)

@views.route("/customerprofile", methods=['POST'])
def customerProfile():
    print(request.args.get('data'))
