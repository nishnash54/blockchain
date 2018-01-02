import requests
from json import dumps

link = 'http://localhost:5000/insert'
#link = 'http://localhost:5000/insert?data={"name": "Nishant", "tid": "0000"}'
name = "Nishant"
tid = "0000"
res = requests.get(url = link, params = { "name": name, "tid": tid})
print res
print res.content
