from hashlib import sha256
from json import dumps, loads

def hash(data):
    print data
    data_hash = sha256(dumps(loads(data), sort_keys=True).encode('utf-8')).hexdigest()
    print data_hash
    return data_hash
