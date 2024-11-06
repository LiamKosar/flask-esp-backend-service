from api.simple_api_responses import ApiResponses
from flask import Flask, jsonify, request
import os

class ApiFunctions:

    ESP_AUTH_KEY = os.getenv('ESP_AUTH_KEY')

    @classmethod
    def update_device_runtime(this):
        
        VERIFICATION_KEY:str = request.headers.get('Authorization', str)
        if VERIFICATION_KEY != this.ESP_AUTH_KEY or VERIFICATION_KEY is None:
            return ApiResponses.simple_unauthorized_request_api_response()
        
        
        return ApiResponses.simple_entry_created_api_response()