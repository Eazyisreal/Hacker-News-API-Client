
import datetime

def parse_datetime(value):
    if isinstance(value, str):
        return datetime.datetime.fromisoformat(value)
    else:
        raise ValueError('Invalid datetime value')
