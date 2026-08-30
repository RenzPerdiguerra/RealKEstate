import os

class BaseConfig():
    # DB
    DB_USER = os.getenv("DB_USER")
    DB_PASS = os.getenv("DB_PASS")
    DB_HOST = os.getenv("DB_HOST")
    DB_NAME = os.getenv("DB_NAME")
    DB_PORT = os.getenv("DB_PORT")
    # Oauth
    # Auth secrets
    
class DevelopmentConfig(BaseConfig):
    Debug = True
    SQLALCHEMY_DATABSE_URL = os.getenv("DATABASE_URL")
    CORS_ORIGINS = [
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "http://localhost:5000",
        "http://127.0.0.1:5000"
    ]
    CSP = "default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline'; connect-src 'self' http://localhost:8000"
    
class StagingConfig(BaseConfig):
    Debug = False
    SQLALCHEMY_DATABASE_URL = "https://"
    CORS_ORIGINS = ["https://staging.myapp.com"]
    CSP = "default-src 'self'; script-src 'self'; style-src 'self'; connect-src 'self' https://staging.myapp.com"

class ProductionConfig(BaseConfig):
    Debug = False
    SQLALCHEMY_dATABASE_URL = ""
    CORS_ORIGINS = ["https://production.myapp.com"]
    CSP = "default-src 'self'; script-src 'self'; style-src 'self'; connect-src 'self' https://production.myapp.com"

config = {
    "development": DevelopmentConfig,
    "staging": StagingConfig,
    "production": ProductionConfig
}

def get_config():
    env = os.getenv("FASTAPI_ENV", "development")
    return config[env]()
    