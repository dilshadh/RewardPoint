from flask import Flask


def create_app(flask_config_name=None):
    app = Flask(__name__)
    import rewardapp.views
    app.config.from_object('config.DevelopmentConfig')
    return app