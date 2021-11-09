from typing import List

from schemas import quotation as quotation_schema

# basic mock data

MOCK_QUOTE_DATA = []

AGE_LOAD: List[quotation_schema.AgeLoad] = [
    {'age': range(18,30+1), 'load': 0.6},
    {'age': range(31,40+1), 'load': 0.7},
    {'age': range(41,50+1), 'load': 0.8},
    {'age': range(51,60+1), 'load': 0.9},
    {'age': range(61,70+1), 'load': 1}
]