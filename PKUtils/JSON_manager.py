import json


def to_JSON(data):
    if data is None:
        return json.dumps(dict())
    return json.dumps(data)

def to_error_JSON(reason: str):
    data = {
        'status': 'error', 
        'reason': reason,
    }
    return to_JSON(data)

def load_to_JSON(data):
    return json.loads(data)