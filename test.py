import requests

link = 'http://localhost:5000/insert'
res = requests.get(url = link, params = {"data": "Nishant"})
print res
print res.content
