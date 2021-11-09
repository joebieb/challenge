from fastapi import status
from fastapi.responses import JSONResponse
from typing import List, Tuple


class CustomResponse(JSONResponse):
    ''' A custom JSONResponse class used to supply custom json response objects 
        that differ from the expected reponse_model of API routes '''
    def __init__(self, status_code: status, message: str, headers: dict):
        self.message = message
        self.content = {'message': message}
        self.raw_headers: List[Tuple[bytes, bytes]] = []
        if headers != None:
            for k,v in headers.items():
                self.headers[k] = v
        super().__init__(status_code=status_code, content=self.content, headers=self.headers)


def json_response_200(message: str = 'OK', headers: dict = None) -> CustomResponse:
    return CustomResponse(status_code=status.HTTP_200_OK, message=message, headers=headers)


def json_response_201(message: str = 'created', headers: dict = None) -> CustomResponse:
    return CustomResponse(status_code=status.HTTP_201_CREATED, message=message, headers=headers)


def json_response_202(message: str = 'accepted', headers: dict = None) -> CustomResponse:
    return CustomResponse(status_code=status.HTTP_202_ACCEPTED, message=message, headers=headers)


def json_response_400(message: str = 'bad request', headers: dict = None) -> CustomResponse:
    return CustomResponse(status_code=status.HTTP_400_BAD_REQUEST, message=message, headers=headers)


def json_response_401(message: str = 'unauthorized', headers: dict = None) -> CustomResponse:
    return CustomResponse(status_code=status.HTTP_401_UNAUTHORIZED, message=message, headers=headers)


def json_response_403(message: str = 'forbidden', headers: dict = None) -> CustomResponse:
    return CustomResponse(status_code=status.HTTP_403_FORBIDDEN, message=message, headers=headers)


def json_response_404(message: str = 'not found', headers: dict = None) -> CustomResponse:
    return CustomResponse(status_code=status.HTTP_404_NOT_FOUND, message=message, headers=headers)


def json_response_422(message: str = 'unprocessable entity', headers: dict = None) -> CustomResponse:
    return CustomResponse(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, message=message, headers=headers)


def json_response_500(message: str = 'unexpected error', headers: dict = None) -> CustomResponse:
    return CustomResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, message=message, headers=headers)