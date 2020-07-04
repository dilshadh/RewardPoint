from rewardapp.model import Customer, Configuration, Rewards
from rewardapp.utils import rewardCalculation
from flask_restful import Resource
from flask import jsonify, request
from flask_jwt_extended import jwt_required
from rewardapp import db
import json

class CustomerApi(Resource):
    def get(self):
        results = []
        customers = Customer.query.filter(Customer.c_active_flag == 1).all()
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
            if customer.c_active_flag == 0:
                return {'error' : 'Customer already exists, but is inactive'} ,401
            return { 'error' : 'Customer already exists' }, 401
        customer = Customer(c_username=c_username,c_name=c_name,c_phone_number=c_phone_number, c_email=c_email)
        db.session.add(customer)
        db.session.commit()
        return {'c_name' : customer.c_name }, 200

class SingleCustomer(Resource):

    def get(self, c_phone_number):
        customer=Customer.query.filter((Customer.c_phone_number == c_phone_number) & (Customer.c_active_flag == 1)).first()
        if customer:
            custObj = customer.__dict__
            del custObj['_sa_instance_state']
            return jsonify(custObj)
        return {'error' : 'Customer not exist'} ,401
        
    
    def delete(self, c_phone_number):
        customer=Customer.query.filter((Customer.c_phone_number == c_phone_number) & (Customer.c_active_flag == 1)).first()
        if customer:
            customer.c_active_flag = 0
            db.session.commit()    
            return {'c_name' : customer.c_name }, 200
        return {'error' : "Customer doesnt exist" }, 401

class CustomerReward(Resource):

    def post(self):
        c_phone_number=request.form['c_phone_number']
        r_fuelamount=request.form['r_fuelamount']
        reward_point = rewardCalculation(r_fuelamount)
        customer=Customer.query.filter((Customer.c_phone_number == c_phone_number) & (Customer.c_active_flag == 1)).first()
        if customer:
            customer_id = customer.c_id
            reward=Rewards(r_fuelamount=r_fuelamount, r_point= reward_point, r_ename="ashiq",r_cutomerid=customer_id)
            db.session.add(reward)
            db.session.commit()
            return {'reward_point': reward_point}
        return {'error' : "Customer doesnt exist" }, 401

class RewardRate(Resource):

    def post(self):
        cnfg_name = request.form['cnfg_name']
        cnfg_value = request.form['cnfg_value']
        config =  Configuration.query.filter(Configuration.cnfg_name == cnfg_name).first()
        if config:
            config.cnfg_value = cnfg_value
            db.session.commit()
            return {'status ' : "Reward rate updated"}, 200 
        else:      
            configuration= Configuration(cnfg_name=cnfg_name, cnfg_value=cnfg_value)    
            db.session.add(configuration)
            db.session.commit()
            return {'status ' : "Reward rate added"}, 200