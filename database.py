from pymongo import MongoClient
from config import var
from json import dumps, loads
from hash_gen import hash

client = MongoClient()
client = MongoClient("mongodb://admin:Admin1#@ds341247.mlab.com:41247/medical_records", 27017)
db = client['medical_records']

def update(data, hash, tid):
    data = loads(data)
    db.blockchain.insert({"patient_id": data['patient_id'],
    "medical_record_id": data['medical_record_id'],\
        "insurance_id": data['insurance_id'],
         "transaction_id": hash, "previous_transaction": tid}
         )

def validate(tid):
    flag = 1
    lst = []
    while(tid!=""):
        try:
            cur = db.blockchain.find({"transaction_id": tid})[0]
        except IndexError:
            flag = 0
            break
        last = cur['previous_transaction']
        #print "tid : ", tid
        #print "last : ", last
        #print "cur : ", cur['transaction_id']
        data = dumps({"patient_id": cur['patient_id'], "medical_record_id": cur['medical_record_id'],\
            "insurance_id": cur['insurance_id'], "last_transaction": cur['previous_transaction']})
        val = hash(data)
        if val!=tid:
            flag = 0
            break
        tid = last
    return str(flag)
