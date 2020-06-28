from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_jwt_extended import JWTManager
from flask_restful import Api
db = SQLAlchemy()
login_manager = LoginManager()

#Method to create flask application with required configuration
def create_app(config_file=None):
    app = Flask(__name__)
    app.config.from_object('config.DevelopmentConfig')
    api = Api(app)
    jwt = JWTManager(app)
    login_manager.init_app(app)
    db.init_app(app)
    from rewardapp.model import Employee, Customer, Rewards, Configuration
    with app.app_context():
        db.create_all()
    from rewardapp.employees import GetEmployee, EmployeeApi
    from rewardapp.auth import LoginApi
    api.add_resource(LoginApi, '/login')
    api.add_resource(GetEmployee, '/getEmployee/<e_username>')
    api.add_resource(EmployeeApi, '/Employee')
    return app