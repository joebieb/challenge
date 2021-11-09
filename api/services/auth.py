from datetime import datetime, timedelta
from jose import jwt
from jose.exceptions import JWTError

from config import settings

def encode_token(email):
    ''' create jwt access token from email and values set in the config.py '''
    try:
        _data = {
            'exp' : datetime.utcnow() + timedelta(minutes=settings.access_token_expiration_minutes),
            'iat' : datetime.utcnow(),
            'scope': 'access_token',
            'sub' : email
        }
        return jwt.encode(_data, settings.secret_key, algorithm=settings.algorithm)
    except Exception:
        raise

def decode_token(token):
    try:
        payload = jwt.decode(token, settings.secret_key, algorithms=[settings.algorithm])
        if (payload['scope'] == 'access_token'):
            return True 
        raise JWTError
    except Exception:
        raise