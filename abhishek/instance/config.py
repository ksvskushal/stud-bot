
class Config(object):
    """Parent configuration class."""
    DEBUG = False
    CSRF_ENABLED = True
    SECRET = 'codingclubiitg'
    SQLALCHEMY_DATABASE_URI = 'postgresql://vivekraj:heysiri@localhost/updates_api'

class DevelopmentConfig(Config):
    """Configurations for Development."""
    DEBUG = True

# class TestingConfig(Config):
#     """Configurations for Testing, with a separate test database."""
#     TESTING = True
#     SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/test_db'
#     DEBUG = True

class StagingConfig(Config):
    """Configurations for Staging."""
    DEBUG = True

class ProductionConfig(Config):
    """Configurations for Production."""
    DEBUG = False
    TESTING = False

app_config = {
    'development': DevelopmentConfig,
    # 'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
}
