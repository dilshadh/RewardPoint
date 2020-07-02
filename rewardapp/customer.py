from rewardapp.model import Customer
from flask_restful import Resource
from flask import jsonify, request
from flask_jwt_extended import jwt_required
from rewardapp import db
import json

class CustomerApi(Resource):
    def get(self):
        results = []
        customers = Customer.query.all()
        if customers:
            for customer in customers:
                custObj = customer.__dict__
                del custObj['_sa_instance_state']
                results.append(custObj)
            return jsonify(results)
        return {'error' : 'Customers doesnt exist'}, 401

    def post(self):
        c_username = request.form['c_username']
        c_name=request.form['c_name']
        c_phone_number=request.form['c_phone_number']
        c_email=request.form['c_email']
        customer = Customer.query.filter((Customer.c_email == c_email) | (Customer.c_phone_number == c_phone_number) | (Customer.c_username == c_username)).first()
        if customer:
            return { 'error' : 'Customer already exists' }, 401
        customer = Customer(c_username=c_username,c_name=c_name,c_phone_number=c_phone_number, c_email=c_email)
        db.session.add(customer)
        db.session.commit()
        return {'c_name' : customer.c_name }, 200

class GetSingleCustomer(Resource):

    def get(self, c_phone_number):
        customer=Customer.query.filter_by(c_phone_number=c_phone_number).first()
        if customer:
            custObj = customer.__dict__
            del custObj['_sa_instance_state']
            return jsonify(custObj)
        return {'error' : 'Customer not exist'} ,401