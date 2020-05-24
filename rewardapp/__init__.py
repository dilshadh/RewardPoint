from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
#Method to create flask application with required configuration
def create_app(config_file=None):
    app = Flask(__name__)
    app.config.from_object('config.DevelopmentConfig')
    db.init_app(app)
    from rewardapp.model import Employee
    with app.app_context():
        db.create_all()
        employee2= Employee('ashiqrahman','ashique','1234567890')
        employee2.set_password('Thasleenababu1@')
        db.session.add(employee2)
        db.session.commit()
        employee = Employee.query.filter_by(e_phone_number='1234567890').first()
        print('password is ',employee.check_password('Thasleenababu1@'))
    from rewardapp.views import views
    app.register_blueprint(views)
    return app