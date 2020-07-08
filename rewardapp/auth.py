from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, login_required, current_user, logout_user
from flask_jwt_extended import create_access_token
from .model import Employee
from rewardapp import db
from flask_restful import Resource
import datetime


class LoginApi(Resource):

    def post(self):
        username = request.form['username']
        password = request.form['password']
        employee = Employee.query.filter_by(e_username=username).first()
        if employee:
            if employee.check_password(password):
                expires = datetime.timedelta(days=7)
                access_token = create_access_token(identity=str(employee.e_username), expires_delta=expires)
                return {'token': access_token}, 200
            return {'error' : 'Password entered is incorrect'}, 401
        return {'error' : 'Employee Not Found'}, 401
