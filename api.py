from flask import Flask, request
from hash_gen import hash
from database import update, validate
from json import dumps

app = Flask(__name__)
last_transaction = ""

@app.route("/")
def api_home():
    return "Blockchain Home"

@app.route("/insert")
def api_transaction():
    global last_transaction
    data = dumps(
        {"patient_id": request.args['patient_id'], 
        "medical_record_id": request.args['medical_record_id'],\
        "insurance_id": request.args['insurance_id'], 
        "last_transaction": last_transaction}
        )
    data_hash = hash(data)
    update(data, data_hash, last_transaction)
    last_transaction = data_hash
    return last_transaction

@app.route("/validate")
def api_validate():
    return validate("6a878b780f041f60c289de001c8a6ae2acee641b3fbf6fe004958cf8aa2e9745")

if __name__ == '__main__':
    app.run(debug = True)
