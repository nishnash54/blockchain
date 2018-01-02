from flask import Flask, request
from hash_gen import hash

app = Flask(__name__)

@app.route("/")
def api_home():
    return "Blockchain Home"

@app.route("/insert")
def api_transaction():
    if 'data' in request.args:
        #return request.args['data']
        return hash(request.args['data'])

if __name__ == '__main__':
    app.run(debug = True)
