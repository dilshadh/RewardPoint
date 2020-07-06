from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_jwt_extended import JWTManager
from flask_restful import Api
db = SQLAlchemy()
login_manager = LoginManager()

#Method to create flask application with required configuration
def create_app():
    app = Flask(__name__)
    app.config.from_object('config.DevelopmentConfig')
    api = Api(app)
    jwt = JWTManager(app)
    login_manager.init_app(app)
    db.init_app(app)
    from rewardapp.model import Employee, Customer, Rewards, Configuration
    with app.app_context():
        db.create_all()
    from rewardapp.employees import SingleEmployee, EmployeeApi
    from rewardapp.auth import LoginApi
    from rewardapp.customer import CustomerApi, SingleCustomer, CustomerReward, RewardRate
    api.add_resource(LoginApi, '/login')
    api.add_resource(SingleEmployee, '/singleEmployee/<e_username>')
    api.add_resource(EmployeeApi, '/employee')
    api.add_resource(CustomerApi, '/customer')
    api.add_resource(SingleCustomer, '/singleCustomer/<c_phone_number>')
    api.add_resource(CustomerReward, '/customerreward')
    api.add_resource(RewardRate, '/rewardrate')
    return app