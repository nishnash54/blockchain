import requests
from json import dumps

link = 'http://localhost:5000/insert'
data = {"from_id": "0000", "to_id": "1234", "transaction_id": "abc"}
res = requests.get(url = link, params = data)
print res
print res.content
