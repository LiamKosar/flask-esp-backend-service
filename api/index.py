from flask import Flask, jsonify, request
from pony.flask import Pony
from pony.orm import Database, Required, db_session, PrimaryKey, Set, Optional
import os
from api.simple_api_responses import ApiResponses
from api.api_functions import ApiFunctions

app = Flask(__name__)
Pony(app)

@app.route('/')
def home():
    # u1 = User(email='meowmir@gmail.com')
    # db.commit()
    return 'Hello, this is a backend service for ESP-Next-Testing'

@app.route('/api/hello', methods=['GET'])
def api_hello():
    if(request.method == 'GET'): 
        data = { 
            "Modules" : 15, 
            "Subject" : "Data Structures and Algorithms", 
        } 
        return jsonify(data)
    return jsonify({"Error: Error"}) 


@app.route('/api/device/connect', methods=['GET'])
def api_device_connect():
    if(request.method == 'GET'): 
        return ApiResponses.simple_device_connected_api_response()
    else:
        return ApiResponses.simple_baq_request_api_response()
        

@app.route('/api/device/update', methods=['POST', 'GET'])
def api_device_update():
    # if(request.method == 'POST'):
    return ApiFunctions.verify_authorized_request(lambda: ApiFunctions.verify_mac_address_exists(lambda: ApiFunctions.update_device_runtime()))

