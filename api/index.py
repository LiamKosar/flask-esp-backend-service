from flask import Flask, jsonify, request
from pony.flask import Pony
from pony.orm import Database, Required, db_session, PrimaryKey, Set, Optional
import os
from api.database_setup import connect_to_database
from api.simple_api_responses import ApiResponses
from api.api_functions import ApiFunctions

app = Flask(__name__)
Pony(app)

db = connect_to_database()


class User(db.Entity):
    _table_ = 'User'
    email = PrimaryKey(str, 255)
    first_name = Optional(str, 50)
    last_name = Optional(str, 50)
    phone_number = Optional(str, 20)
    devices = Set('Device')
    vehicles = Set('Vehicle')

class Device(db.Entity):
    _table_ = 'device'
    mac_address = PrimaryKey(str, 17)
    version = Required(str, 10)
    runtime = Optional(float, default=0)
    date_updated = Required(str, 50)
    user = Optional(User, reverse='devices', column='user_email', default='kosar.liam@gmail.com')
    vehicle = Optional('Vehicle', reverse='device')

class MaintenanceProcedure(db.Entity):
    _table_ = 'maintenanceprocedure'
    id = PrimaryKey(int, auto=True)
    # vehicle_id = Required(int)
    name = Required(str, 100)
    description = Optional(str)
    interval = Required(float)
    current_interval = Optional(float, default=0)
    vehicle = Required('Vehicle', reverse='maintenance_procedures', column="vehicle_id")

class Vehicle(db.Entity):
    _table_ = 'vehicle'
    vehicle_id = PrimaryKey(int, auto=True)
    # user_email = Required(str, 255)
    name = Required(str, 100)
    # mac_address = Optional(str, 17, unique=True)
    runtime = Optional(float, default=0)
    image_url = Optional(str, 255)
    date_updated = Required(str, 50)
    device = Optional(Device, reverse='vehicle', column="mac_address", unique=True)
    user = Required(User, reverse='vehicles', column="user_email")
    maintenance_procedures = Set(MaintenanceProcedure)

db.generate_mapping(create_tables=False)

@app.route('/')
def home():
    u1 = User(email='meowmir@gmail.com')
    db.commit()
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
    return ApiFunctions.update_device_runtime()

