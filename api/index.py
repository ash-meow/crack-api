from flask import Flask
from flask import request
from flask import jsonify
from time import time
app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/license/id/core/<id>')
def core(id):
    return jsonify({
        "owner": "ch1ppie",
        "product": "DonutCore",
        "ips": [request.remote_addr],
        "creation_date": time()
    }), 200
@app.route('/license/zel/id/<id>')
def zel(id):
    return jsonify({
        "owner": "ch1ppie",
        "product": "ZelAuction",
        "ips": [request.remote_addr],
        "creation_date": time()
    }), 200
