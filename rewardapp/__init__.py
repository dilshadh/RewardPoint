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
    from rewardapp.views import views
    app.register_blueprint(views)
    return app