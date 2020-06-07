from flask import Blueprint, render_template, request, flash
from flask_login import login_required
from rewardapp.forms.emp_forms import LoginForm, EmployeeRegForm
from rewardapp.model import Customer, Employee, Rewards
from rewardapp import db
from datetime import datetime
views = Blueprint('views', __name__, template_folder="templates")

@views.route("/", methods=['GET'])
def mainPage():
    return render_template("base.html")      

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
    customer_number="9895059403"
    customer_id=Customer.query.filter_by(c_phone_number=customer_number).first()
    cust_id= customer_id.c_id
    reward=Rewards(r_point=100, r_ename="ashiq",r_cutomerid=cust_id)
    print(reward.r_ename)
    db.session.add(reward)
    db.session.commit()
    return "hi"