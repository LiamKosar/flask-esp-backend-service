from flask import Flask, jsonify, request

app = Flask(__name__)

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