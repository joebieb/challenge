from fastapi import APIRouter

from services import auth as auth_service
from schemas import auth as auth_schema
from shared.http_responses import json_response_500


router = APIRouter(
    prefix='/api',
    tags=['Auth']
)


@router.post("/auth/token", response_model=auth_schema.Token, responses={})
async def create_token(user: auth_schema.User):
    ''' create a jwt to use on subsequent requests '''
    # TODO: replace this route with a login route to retrieve token
    # or use a third party for authentication and authorization
    try:
        return auth_schema.Token(
            access_token = auth_service.encode_token(user.email)
        )        
    except Exception as e:
        return json_response_500(message='Could not retrieve token')