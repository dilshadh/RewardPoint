from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, login_required, current_user, logout_user
from flask_jwt_extended import create_access_token
from .model import Employee
from rewardapp import db
from flask_restful import Resource
from flask import request
import datetime


class LoginApi(Resource):

    def post(self):
        body = request.get_json()
        username =  body.get('username')
        password = body.get('password')
        employee = Employee.query.filter_by(e_username=username).first()
        if employee:
            if employee.check_password(password):
                expires = datetime.timedelta(days=7)
                access_token = create_access_token(identity=str(employee.e_phone_number), expires_delta=expires)
                return {'token': access_token}, 200
            return {'error' : 'Password entered is incorrect'}, 401
        return {'error' : 'Employee Not Found'}, 401


'''

@auth.route('/',methods=['GET'])
def home():
    return redirect(url_for('auth.login'))

@auth.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    print("jhi")
    if form.validate_on_submit():
        print('validated on submit')
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
            return render_template('index.html',title='Login', form=form)
        flash('UserName doesnt exists!','danger')
    return render_template('index.html',title='Login', form=form)

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


'''