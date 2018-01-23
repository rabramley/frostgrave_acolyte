class BaseConfig(object):
    """Standard configuration options"""
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    WTF_CSRF_ENABLED = True
    SECRET_KEY = "secret"


class TestConfig(BaseConfig):
    """Configuration for general testing"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    WTF_CSRF_ENABLED = False


class TestConfigCRSF(TestConfig):
    """Configuration for testing CRSF"""
    WTF_CSRF_ENABLED = True
