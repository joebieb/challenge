from fastapi import FastAPI
from fastapi.param_functions import Depends
from fastapi.staticfiles import StaticFiles
from fastapi.security import HTTPBearer
from fastapi.middleware.cors import CORSMiddleware
from jose import JWTError

from config import settings
from shared.http_responses import json_response_401, json_response_500
from routers import quotation, auth


app = FastAPI(
    title=settings.api_title,
    description=settings.api_description,
    version=settings.api_version
)

# allow all origins to prevent problems while testing
origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(auth.router)
app.include_router(quotation.router)


custom_auth_scheme = HTTPBearer(auto_error=False)

# just a test route
@app.get('/secure', tags=['Test Secure'])
async def index(token: str = Depends(custom_auth_scheme)):
    ''' route to test token in header '''
    try:
        if token == None:
            raise JWTError
        return token
    except JWTError:
        return json_response_401(headers = {'WWW-Authenticate':'Bearer'})
    except Exception:
        return json_response_500()


# keep this route at the bottom so it does not interfere with the other routes
# we are hosting and serving the UI static files here
app.mount('/', StaticFiles(directory='static', html=True), name='static')

# TODO: handle 404 for all other routes