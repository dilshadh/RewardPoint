class Config(object):
    DEBUG = False
    TESTING = False

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    FLASK_DEBUG = 1
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://admin:Admin123@database-1.cp61wyr1b7dt.us-east-1.rds.amazonaws.com/root"

class TestingConfig(Config):
    TESTING = False