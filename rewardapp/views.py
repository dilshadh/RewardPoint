from flask import Blueprint, render_template, request, flash, jsonify, Response, redirect, url_for
from flask_login import login_required
from rewardapp.forms.cust_forms import CustomerRegistrationForm, SearchCustomerForm
from rewardapp.model import Customer, Employee
from rewardapp import db
import json
views = Blueprint('views', __name__, template_folder="templates")

@views.route("/homePage", methods=['GET'])
@login_required
def homePage():
    return render_template("homePage.html")

@views.route("/employeeRegistration", methods=['GET','POST'])
@login_required
def empRegistration():
    form=EmployeeRegForm()
    if form.validate_on_submit():
        e_username = form.userName.data
        e_password=form.password.data
        e_name=form.empName.data
        e_phone_number=form.phonenumber.data
        employee = Employee.query.filter_by(e_phone_number=e_phone_number).first()
        if employee:
            flash('Phone Number Already Exists!','danger')
            return render_template('employeeRegistration.html',title='Employee Registration', form=form)
        employee = Employee(e_username=e_username,e_name=e_name,e_phone_number=e_phone_number)
        employee.set_password(e_password)
        db.session.add(employee)
        db.session.commit()
        flash('Employee Added Successfully!','success')
    return render_template("employeeRegistration.html",title='Employee Registration', form=form)    

@views.route("/rewaddemo", methods=['GET'])
def rewadDemo():
    reward_point = rewardCalculation(1000, 1)
    print(reward_point)
    customer_number="9895059403"
    customer_id=Customer.query.filter_by(c_phone_number=customer_number).first()
    cust_id= customer_id.c_id
    reward=Rewards(r_fuelamount=1000, r_point= reward_point, r_ename="ashiq",r_cutomerid=cust_id)
    print(reward.r_ename)
    db.session.add(reward)
    config=Configuration.query.get(1)
    config.cnfg_name="reward_rate"
    config.cnfg_value=2
    db.session.commit()
    return "hi"
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
