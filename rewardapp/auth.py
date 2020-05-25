from flask import Blueprint, render_template, request, flash
from flask_login import login_user, login_required, current_user, logout_user
from .model import Employee
from rewardapp import db

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/login',methods=['POST'])
def loginPost():
    username =  request.form.get('username')
    password = request.form.get('password')
    employee = Employee.query.filter_by(e_username=username).first()
    if employee:
        if employee.check_password(password):
            employee.authenticated = True
            login_user(employee, remember=True)
            return render_template('homePage.html')
        flash('Password Entered is Incorrect!')
        return render_template('login.html')
    flash('UserName doesnt exists!')
    return render_template('login.html')

@auth.route('/signup')
@login_required
def signup():
    print('user name is',current_user.get_id())
    return render_template('signup.html',current_user=current_user)

@auth.route('/logout')
@login_required
def logout():
    current_user.authenticated = True
    logout_user()
    return render_template('login.html')
