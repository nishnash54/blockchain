from pymongo import MongoClient
from config import var
from json import loads

client = MongoClient()
client = MongoClient(var.link, 27017)
db = client['blockchain']

def update(data, hash, tid):
    data = loads(data)
    db.transactions.insert({"from_id": data['from_id'], "to_id": data['to_id'],\
        "last_item_transaction": data['transaction_id'], "transaction_id": hash, "previous_transaction": tid})
