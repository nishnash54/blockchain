from flask import Flask, request
from hash_gen import hash
from database import update

app = Flask(__name__)

@app.route("/")
def api_home():
    return "Blockchain Home"

@app.route("/insert")
def api_transaction():
    if 'data' in request.args:
        #return request.args['data']
        data = request.args['data']
        data_hash = hash(data)
        update(data, data_hash)
        return data_hash

if __name__ == '__main__':
    app.run(debug = True)
