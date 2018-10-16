import os

class BaseConfig(object):
    SECRET_KEY = os.getenv("SECRET_KEY", "notsosecret")

class Development(BaseConfig):
    DEBUG = True
    ENV = "development"


class Production(BaseConfig):
    DEBUG = False
    TESTING = False
    ENV = "production"


class Testing(BaseConfig):
    DEBUG = False
    TESTING = True
    ENV = "testing"

configurations = {
    "development": Development,
    "testing": Testing,
    "production": Production
}