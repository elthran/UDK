import os


DATABASE_NAME = os.environ['MYSQL_DATABASE']
USER = os.environ['MYSQL_USER']
DB_PASSWORD = os.environ['MYSQL_ROOT_PASSWORD']
HOST = "mysql"
OPTIONS = "charset=utf8"
MYSQL_BASE = "mysql+mysqldb://{user}:{password}@{host}/{dbname}?{options}"


class BaseConfig:
    """Base configuration."""
    ENV = 'base'
    DEBUG = False
    BCRYPT_LOG_ROUNDS = 13
    THREADS_PER_PAGE = 2
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SQLALCHEMY_ENGINE_OPTIONS = {}
    # I don't know what these do but we might need them at some point.
    # from server show global variables like '%connections%';
    SQLALCHEMY_ENGINE_OPTIONS['pool_size'] = 5000
    SQLALCHEMY_ENGINE_OPTIONS['pool_recycle'] = 30 * 60 # 30 minutes, sounded reasonable?
    # sounded reasonable, maybe should be same as SQLALCHEMY_POOL_RECYCLE
    SQLALCHEMY_ENGINE_OPTIONS['pool_timeout'] = 30

    SQLALCHEMY_DATABASE_URI = MYSQL_BASE.format(user=USER,
                                                password=DB_PASSWORD,
                                                host=HOST,
                                                dbname=DATABASE_NAME,
                                                options=OPTIONS)


class ProductionConfig(BaseConfig):
    ENV = 'production'
    DEBUG = False
    SQLALCHEMY_POOL_RECYCLE = 299  # 1s less than PythonAnywhere's 300s (5 min).


class DevelopmentConfig(BaseConfig):
    """Development configuration."""
    ENV = 'development'
    DEBUG = True
    SSLIFY_DISABLE = True


class TestConfig(BaseConfig):
    ENV = 'test'
    DEBUG = True
    TESTING = True
    PRESERVE_CONTEXT_ON_EXCEPTION = False
