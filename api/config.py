import os
from pydantic import BaseSettings
from fastapi.security import HTTPBearer

class Settings(BaseSettings):
    ''' application configuration
        usage: from config import settings
        access: settings.some_property 
    '''
    api_title: str = 'Coding Challenge API'
    api_description: str = 'API to complete a coding challenge that returns insurance quotes'
    api_version: str = os.getenv('API_VERSION')
    mode: str = os.getenv('MODE')
    access_token_expiration_minutes: int = 30
    algorithm: str = 'HS256'
    secret_key: str = os.getenv('SECRET_KEY')
    default_fixed_rate: int = 3
    default_token_auth_scheme = HTTPBearer(auto_error=False)

    class Config:
        env_file = '.env'

settings = Settings()