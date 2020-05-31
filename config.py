class Config(object):
    DEBUG = False
    TESTING = False

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///schools.sqlite3"
    SECRET_KEY = b'_5#y2L"F4Q8z\n\xec]/'
    WTF_CSRF_ENABLED = True
class TestingConfig(Config):
    TESTING = False