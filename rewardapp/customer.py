from rewardapp.model import Customer, Configuration, Rewards, Employee, Feedback
from rewardapp.utils import rewardCalculation, isAdmin
from flask_restful import Resource
from flask import jsonify, request
from rewardapp import db
import json
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)

class CustomerApi(Resource):
    @jwt_required
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

    @jwt_required
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
    
    @jwt_required
    def get(self, c_phone_number):
        customer=Customer.query.filter((Customer.c_phone_number == c_phone_number) & (Customer.c_active_flag == 1)).first()
        if customer:
            custObj = customer.__dict__
            del custObj['_sa_instance_state']
            return jsonify(custObj)
        return {'error' : 'Customer not exist'} ,401
        
    @jwt_required
    def delete(self, c_phone_number):
        customer=Customer.query.filter((Customer.c_phone_number == c_phone_number) & (Customer.c_active_flag == 1)).first()
        if customer:
            customer.c_active_flag = 0
            db.session.commit()    
            return {'c_name' : customer.c_name }, 200
        return {'error' : "Customer doesnt exist" }, 401

class CustomerReward(Resource):

    @jwt_required
    def post(self):
        c_phone_number=request.form['c_phone_number']
        r_fuelamount=request.form['r_fuelamount']
        config = Configuration.query.get(1)
        reward_point = rewardCalculation(r_fuelamount)
        reward_points = reward_point(config.cnfg_value)
        customer=Customer.query.filter((Customer.c_phone_number == c_phone_number) & (Customer.c_active_flag == 1)).first()
        if customer:
            customer_id = customer.c_id
            e_username = get_jwt_identity()
            employee = Employee.query.filter(Employee.e_username == e_username).first()
            e_id = employee.e_id
            reward=Rewards(r_fuelamount=r_fuelamount, r_point= reward_points, r_employeeid=e_id, r_cutomerid=customer_id)
            db.session.add(reward)
            db.session.commit()
            return {'reward_point': reward_points}
        return {'error' : "Customer doesnt exist" }, 401

class RewardRate(Resource):

    @jwt_required
    def post(self):
        if isAdmin(get_jwt_identity()):
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
        return {'error' : 'Authorization error, Admin privilege required!'}, 403

class CustomerFeedbacks(Resource):
    
    @jwt_required
    def post(self):
        fdb_emprating = request.form['fdb_emprating']
        fdb_servicerating = request.form['fdb_servicerating']
        fdb_comments = request.form['fdb_comments']
        c_phone_number = request.form['c_phone_number']
        customer=Customer.query.filter((Customer.c_phone_number == c_phone_number) & (Customer.c_active_flag == 1)).first()
        e_username = get_jwt_identity()
        employee = Employee.query.filter(Employee.e_username == e_username).first()
        e_id = employee.e_id
        if customer:
            c_id = customer.c_id
            print (e_id)
            feedbacks = Feedback(fdb_emprating=fdb_emprating, fdb_servicerating=fdb_servicerating, fdb_comments=fdb_comments, fdb_cutomerid=c_id, fdb_employeeid=e_id)
            db.session.add(feedbacks)
            db.session.commit()
            return {'status': "Feedbacks added"}, 200
        return {'error' : "Customer doesnt exist"}, 401

class TotalReward(Resource):
    def get(self, c_phone_number):
        customer=Customer.query.filter((Customer.c_phone_number == c_phone_number) & (Customer.c_active_flag == 1)).first()
        if customer:
            points =[value for value, in Rewards.query.join(Customer, Rewards.r_cutomerid==Customer.c_id).filter(Customer.c_phone_number==c_phone_number).values(Rewards.r_point)] 
            return {'Total Points': sum(points)}, 200
        return {'error' : "Customer doesnt exist"}, 401