from flask import Flask, jsonify, request
from pony.flask import Pony
from api.simple_api_responses import ApiResponses
from api.api_functions import ApiFunctions
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
Pony(app)

@app.route('/')
def home():
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
        
# Allows a Device to update the server with its runtime
# Flow looks like this:
#   1) Check if Bearer Token is valid
#   2) Check if there is a mac_address in body, and if it exists in database
#   3) Try to update database, and any corresponding tables (Vehicle, MaintenanceProcedure)
@app.route('/api/device/update', methods=['POST'])
def api_device_update():
    return ApiFunctions.verify_authorized_device_request(
        lambda: ApiFunctions.verify_mac_address_exists(
            lambda: ApiFunctions.update_device_runtime()))

@app.route('/api/user/register', methods=['POST'])
def register_user():
    return ApiFunctions.verify_authorized_user_request(
        lambda: ApiFunctions.verify_email_given_and_not_exists(
            lambda: ApiFunctions.insert_new_user()))