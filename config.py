class Config(object):
    DEBUG = False
    TESTING = False

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = True
    ENV = "development"
    PORT = "8000"
    SQLALCHEMY_DATABASE_URI = "sqlite:///schools.sqlite3"
    SECRET_KEY = b'_5#y2L"F4Q8z\n\xec]/'
    JWT_SECRET_KEY = 't1NP63m4wnBg6nyHYKfmc2TpCOGI4nss'
    WTF_CSRF_ENABLED = True
class TestingConfig(Config):
    TESTING = False