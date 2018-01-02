from hashlib import sha256
from json import dumps, loads

def hash(data):
    #data_hash = sha256(dumps(loads(data), sort_keys=True).encode('utf-8')).hexdigest()
    data_hash = sha256(data.encode('utf-8')).hexdigest()
    return data_hash
