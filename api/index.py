from flask import Flask
from flask import request
from flask import jsonify
from time import time
app = Flask(__name__)

@app.route('/')
def home():
    return 'hii :D'

@app.route('/license/id/core/<id>') # DonutCore
def core(id):
    return jsonify({
        "owner": "ch1ppie",
        "product": "DonutCore",
        "ips": [request.remote_addr],
        "creation_date": time()
    }), 200
@app.route('/license/zel/id/<id>') # ZelAuctions
def zel(id):
    return jsonify({
        "owner": "ch1ppie",
        "product": "ZelAuction",
        "ips": [request.remote_addr],
        "creation_date": time()
    }), 200
@app.route('/api/client', methods = ['POST', 'GET']) # DonutDuels
def duelscheck():
    hwid = request.args.get('hwid')
    product = request.args.get('product')
    key = request.args.get('licenseKey')

    return jsonify({
        "version": "1.5",
        "status_overview": "success",
        "status_msg": "meow cracked",
        "status_id": "200",
        "status_code": 200,
        "main_class": "space.hugster.duels.DuelsPlugin",
        "plugin_data": "plugin data here",
        "clientname": "ch1ppie",
        "discord_username": "ch1ppie",
        "discord_tag": "uwu",
        "discord_id": "0w0"
    }), 200
    
@app.route('/api/authenticate', methods = ['POST']) # DonutDuels
def duelsauth():
    return jsonify({
        "token": "meowmeowmrrp"
    }), 200
