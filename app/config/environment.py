from app.config import private_config

DATABASE_NAME = "UDK"
USER = "UDK_jbrunner"
DB_PASSWORD = private_config.DB_PASSWORD
HOST = "localhost"
OPTIONS = "charset=utf8"
MYSQL_BASE = "mysql+mysqldb://{user}:{password}@{host}/{dbname}?{options}"


class BaseConfig:
    """Base configuration."""
    ENV = 'base'
    DEBUG = False
    BCRYPT_LOG_ROUNDS = 13
    THREADS_PER_PAGE = 2
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # I don't know what these do but we might need them at some point.
    # from server show global variables like '%connections%';
    SQLALCHEMY_POOL_SIZE = 5000
    SQLALCHEMY_POOL_RECYCLE = 30 * 60  # 30 minutes, sounded reasonable?
    # sounded reasonable, maybe should be same as SQLALCHEMY_POOL_RECYCLE
    SQLALCHEMY_POOL_TIMEOUT = 30
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
