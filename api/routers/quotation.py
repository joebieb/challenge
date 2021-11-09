from decimal import Decimal
from fastapi import APIRouter
from fastapi.param_functions import Depends
from fastapi.security.http import HTTPAuthorizationCredentials
from jose import jwt, JWTError
from pydantic import ValidationError

from config import settings
from shared.http_responses import json_response_401, json_response_500
from services import quotation as quotation_service, auth as auth_service
from schemas import quotation as quotation_schema

router = APIRouter(
    prefix='/api',
    tags=['Quotation']
)


@router.post('/quotation', response_model=quotation_schema.QuotationResponse, responses={})
async def quotation(data: quotation_schema.QuotationRequest, 
    token: HTTPAuthorizationCredentials = Depends(settings.default_token_auth_scheme)):
    ''' supplying a valid request object of QuotationRequest and a valid access_token,
        calculate appropriate rate and return a QuotationResponse object,
        otherwise return a validation error        
    '''
    try:
        # let's check the token
        if token == None:
            raise JWTError
        if not auth_service.decode_token(token.credentials):
            raise
        
        # TODO: how should age less than 18 and above 70 be handled
        # since there were no load values associated with those scenarios? error? ignore? 
        # we will ignore for now
        # TODO: determine if there are different fixed rates for different currency types
        # using default_fixed_rate value set in config

        # inclusively get number of days
        _days = (data.end_date - data.start_date).days + 1
        # calculate quote total
        _total = Decimal('{0:.2f}'.format(quotation_service.calculate_rate(settings.default_fixed_rate, data.age, _days)))

        # create mock data entry
        _current_record: dict = quotation_service.mock_data_create(_total, data.currency_id)

        # build response object from most recent data entry
        _response = quotation_schema.QuotationResponse(
            total = _current_record.get('total'),
            currency_id = _current_record.get('currency_id'),
            quotation_id = _current_record.get('quotation_id')
        )

        return _response
    except jwt.ExpiredSignatureError:
        return json_response_401(message='token expired', headers = {'WWW-Authenticate':'Bearer'})
    except JWTError:
        return json_response_401(message='token invalid', headers = {'WWW-Authenticate':'Bearer'})
    except ValidationError as e:
        return e
    except Exception as e:
        return json_response_500('something unexpected has happened')