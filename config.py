import os

class Config:
    """
    """
   SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://daud:jinkoos@localhost/blog'
   SQLALCHEMY_TRACK_MODIFICATIONS = False
 
class ProdConfig(Config):
    """
    """
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    pass

class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}