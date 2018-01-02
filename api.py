from flask import Flask, request
from hash_gen import hash
from database import update
from json import dumps

app = Flask(__name__)

@app.route("/")
def api_home():
    return "Blockchain Home"

@app.route("/insert")
def api_transaction():
    data = dumps({"name": request.args['name'], "tid": request.args['tid']})
    data_hash = hash(data)
    update(data, data_hash)
    return data_hash

if __name__ == '__main__':
    app.run(debug = True)
