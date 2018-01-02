from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def api_transaction():
    return "Home"

if __name__ == '__main__':
    app.run(debug = True)
