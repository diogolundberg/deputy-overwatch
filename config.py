
class Config(object):
    DEBUG = False
    TESTING = False

class Production(Config):
    pass

class Development(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///overwatch_develop'

class Testing(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
