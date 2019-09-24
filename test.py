import requests
from json import dumps

link = 'http://localhost:5000/insert'
data = {"patient_id": "0000", "medical_record_id": "1234", "insurance_id": "abc"}
for i in range(3):
    print "Enter patient_id: "
    fid = raw_input().strip()
    print "Enter medical_record_id: "
    toid = raw_input().strip()
    print "Enter insurance_id:"
    lt = raw_input().strip()
    data = {"patient_id": fid, "medical_record_id": toid, "insurance_id": lt}
    res = requests.get(url = link, params = data)
    print res
    print res.content
