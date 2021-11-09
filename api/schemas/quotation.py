from decimal import Decimal
from datetime import date
from typing import List
from enum import Enum
from pydantic import BaseModel, Field, validator


class CurrencyId(str, Enum):
    EUR = 'EUR'
    GBP = 'GBP'
    USD = 'USD'


class AgeLoad(BaseModel):
    age: range
    load: Decimal
    
    # TODO: range validator
    # @validator('age')

    class Config:
        # there is no default validator in pydantic for range
        arbitrary_types_allowed = True


class QuotationRequest(BaseModel):
    age: List[int] = Field(min_items=1)
    currency_id: CurrencyId
    start_date: date
    end_date: date

    @validator('age')
    def first_age_value(cls, v):
        if v[0] < 18:
            raise ValueError('First age value must be 18 or greater')
        return v

    @validator('age')
    def minimum_age(cls, v):
        if 0 in v:
            raise ValueError('Age of 0 is invalid')
        return v
    
    @validator('end_date')
    def start_date_before_end(cls, v, values):
        _start = values.get('start_date')
        if _start != None and _start > v:
            raise ValueError('Start date must be before end date')
        return v

    # TODO: additional validations
    

class QuotationResponse(BaseModel):
    total: Decimal
    currency_id: CurrencyId
    quotation_id: int