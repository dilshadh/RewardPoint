from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, login_required, current_user, logout_user
from .model import Employee
from rewardapp import db
from flask import request
from rewardapp.forms.emp_forms import LoginForm
auth = Blueprint('auth', __name__)


@auth.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username =  form.username.data
        password = form.password.data
        employee = Employee.query.filter_by(e_username=username).first()
        if employee:
            if employee.check_password(password):
                employee.authenticated = True
                login_user(employee, remember=form.remember.data)
                next_page = request.args.get('next')
                return redirect(next_page) if next_page else redirect(url_for('views.homePage'))
            flash('Password Entered is Incorrect!','danger')
            return render_template('login.html',title='Login', form=form)
        flash('UserName doesnt exists!','danger')
    return render_template('login.html',title='Login', form=form)

@auth.route('/signup')
@login_required
def signup():
    print('user name is',current_user.get_id())
    return render_template('signup.html',current_user=current_user)

@auth.route('/logout')
@login_required
def logout():
    form = LoginForm()
    employee = current_user
    employee.authenticated = False
    logout_user()
    return redirect(url_for('auth.login'))

@auth.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


