class Config(object):
    DEBUG = False
    TESTING = False

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True
    DB_NAME = "development_db"
    DB_URI = "mysql:root/"

class TestingConfig(Config):
    TESTING = False