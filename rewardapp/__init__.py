from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#Method to create flask application with required configuration
def create_app(config_file=None):
    app = Flask(__name__)
    app.config.from_object('config.DevelopmentConfig')
    db.init_app(app)
    from rewardapp.model import UserDilshad
    with app.app_context():
        admin = UserDilshad('admin1234', 'admin1234@example.com','dilsahd')
        db.create_all()
        db.session.add(admin)
        db.session.commit()
    from rewardapp.views import views
    app.register_blueprint(views)
    return app