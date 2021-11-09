from decimal import Decimal
from typing import List

from schemas import quotation as quotation_schema
from db import MOCK_QUOTE_DATA as quotes, AGE_LOAD as age_load


def get_load(age: int) -> Decimal:
    ''' return a load value based on a given age '''
    try:
        for row in age_load:
            if age in row.get('age'):
                return row.get('load')  
        # TODO: handle age out of range
        # until it is determined how to handle an age out of range
        # return 0.0 instead of None to prevent errors in calling function
        return 0.0
    except Exception:
        raise


def calculate_rate(fixed_rate: int, age: List[int], days: int) -> Decimal:
    ''' calculate rate on each age provided and accumulate the total
        formula: rate * load * days 
    '''
    try:
        _rates = [fixed_rate * get_load(x) * days for x in age]
        return sum(_rates)
    except Exception:
        raise 


def mock_data_create(total: Decimal, currency_id: quotation_schema.CurrencyId) -> dict:
    ''' add a row to mock data and return the last(current) dictionary object '''
    try:
        _idx = len(quotes) + 1
        quotes.append({
            'total': total,
            'currency_id': currency_id,
            'quotation_id': _idx
        })
        return quotes[len(quotes)-1]
    except Exception:
        raise