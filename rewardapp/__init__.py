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
    from rewardapp.model import Employee, Customer, Rewards, Configuration, Feedback
    with app.app_context():
        db.create_all()
        employee = Employee.query.filter(Employee.e_username =='admin').first()
        if not employee:
            employee = Employee(e_username='admin',e_name='Administrator',e_phone_number='0000000000', e_admin =1)
            employee.set_password('4@fxep6%qrs93#qws')
            db.session.add(employee)
            db.session.commit()
    from rewardapp.employees import SingleEmployee, EmployeeApi, EmpAverageRating, AverageServiceRating
    from rewardapp.auth import LoginApi
    from rewardapp.customer import CustomerApi, SingleCustomer, CustomerReward, RewardRate, CustomerFeedbacks, TotalReward
    api.add_resource(LoginApi, '/login')
    api.add_resource(SingleEmployee, '/singleEmployee/<e_username>')
    api.add_resource(EmployeeApi, '/employee')
    api.add_resource(CustomerApi, '/customer')
    api.add_resource(SingleCustomer, '/singleCustomer/<c_phone_number>')
    api.add_resource(CustomerReward, '/customerreward')
    api.add_resource(RewardRate, '/rewardrate')
    api.add_resource(CustomerFeedbacks, '/feedback')
    api.add_resource(TotalReward, '/totalpoints/<c_phone_number>')
    api.add_resource(EmpAverageRating, '/empaveragerating/<e_username>')
    api.add_resource(AverageServiceRating, '/averageservicerating')
    return app