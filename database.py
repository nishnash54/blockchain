from pymongo import MongoClient
from config import var

client = MongoClient()
client = MongoClient(var.link, 27017)
db = client['blockchain']

def update(data, hash):
    db.transactions.insert({"data": data, "transaction_id": hash})
