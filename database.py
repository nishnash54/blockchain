from pymongo import MongoClient
from config import var
from json import dumps, loads
from hash_gen import hash

client = MongoClient()
client = MongoClient(var.link, 27017)
db = client['subconn']

def update(data, hash, tid):
    data = loads(data)
    db.blockchain.insert({"from_id": data['from_id'], "to_id": data['to_id'],\
        "last_item_transaction": data['transaction_id'], "transaction_id": hash, "previous_transaction": tid})

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
        data = dumps({"from_id": cur['from_id'], "to_id": cur['to_id'],\
            "transaction_id": cur['last_item_transaction'], "last_transaction": cur['previous_transaction']})
        val = hash(data)
        if val!=tid:
            flag = 0
            break
        tid = last
    return str(flag)
