from flask import jsonify, request
from flask_jwt_extended import jwt_required
from flask_restful import Resource
from rewardapp.model import Employee, Rewards, Configuration
from rewardapp import db
import json
class GetEmployee(Resource):
    
    def get(self, e_username):
        employee = Employee.query.filter_by(e_username=e_username).first()
        if employee:
            return jsonify(employee)
        return {'error' : 'Employee doesnt exist'}, 401

class EmployeeApi(Resource):

    def get(self):
        results = []
        employees = Employee.query.all()
        if employees:
            for employee in employees:
                empObj = employee.__dict__
                del empObj['_sa_instance_state']
                results.append(empObj)
            return jsonify(results)
        return {'error' : 'Employees doesnt exist'}, 401

    def post(self):
        e_username = request.form['e_username']
        e_password = request.form['e_password']
        e_name=request.form['e_name']
        e_phone_number=request.form['e_phone_number']
        employee = Employee.query.filter((Employee.e_phone_number == e_phone_number) | (Employee.e_username == e_username)).first()
        if employee:
            return { 'error' : 'Employee already exists' }, 401
        employee = Employee(e_username=e_username,e_name=e_name,e_phone_number=e_phone_number)
        employee.set_password(e_password)
        db.session.add(employee)
        db.session.commit()
        return {'e_id' : employee.e_id }, 200