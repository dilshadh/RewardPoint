from flask import Flask, Blueprint

from .views import views
def create_app(config_file=None):
    app = Flask(__name__)
    app.config.from_object('config.DevelopmentConfig')
    app.register_blueprint(views)
    return app