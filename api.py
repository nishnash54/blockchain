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
    data = dumps({"from_id": request.args['from_id'], "to_id": request.args['to_id'],\
        "transaction_id": request.args['transaction_id'], "last_transaction": last_transaction})
    data_hash = hash(data)
    update(data, data_hash, last_transaction)
    last_transaction = data_hash
    return last_transaction

@app.route("/validate")
def api_validate():
    return validate("3b7011da3be422a3afc91d31cb824281b051c3e7fa924a871722f04f6d134965")

if __name__ == '__main__':
    app.run(debug = True)
