from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
db = SQLAlchemy()
login_manager = LoginManager()

#Method to create flask application with required configuration
def create_app(config_file=None):
    app = Flask(__name__)
    app.config.from_object('config.DevelopmentConfig')
    login_manager.init_app(app)
    db.init_app(app)
    from rewardapp.model import Employee, Customer, Rewards
    with app.app_context():
        db.create_all()
       
    from rewardapp.views import views
    from rewardapp.auth import auth
    app.register_blueprint(views)
    app.register_blueprint(auth)
    login_manager.login_view = "auth.login"
    return app