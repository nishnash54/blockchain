import requests
from json import dumps

link = 'http://localhost:5000/insert'
data = {"from_id": "0000", "to_id": "1234", "transaction_id": "abc"}
for i in range(6):
    print "Enter from_id: "
    fid = raw_input().strip()
    print "Enter to id:"
    toid = raw_input().strip()
    print "Enter last item transaction: "
    lt = raw_input().strip()
    data = {"from_id": fid, "to_id": toid, "transaction_id": lt}
    res = requests.get(url = link, params = data)
    print res
    print res.content
