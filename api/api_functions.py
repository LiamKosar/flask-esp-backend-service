from api.simple_api_responses import ApiResponses
from flask import request
import os
from api.database_functions import DatabaseFunctions

class ApiFunctions:

    # Auth for ESP Device
    ESP_AUTH_KEY = os.getenv('ESP_AUTH_KEY')
    
    # Auth for User activities
    REGISTER_USER_AUTH = os.getenv('REGISTER_USER_AUTH')

    # Updates the runtime for a specific device
    # Outcomes:
    #   - Missing runtime_hrs -> Bad Request
    #   - Update runtime for the device, and POTENTIALLY an associated vehicle/set of maintenance procedures
    #   - Success -> Return successful entry updated     
    @classmethod
    def update_device_runtime(this):
        data = request.get_json()
        mac_address = data.get('mac_address')
        runtime_hrs = data.get('runtime_hrs')

        # Check if missing required fields
        if runtime_hrs is None:
            return ApiResponses.simple_baq_request_api_response_with_missing_parameter("runtime_hrs")

        try:
            DatabaseFunctions.update_device_runtime(mac_address=mac_address, runtime_hrs=runtime_hrs)
            return ApiResponses.simple_entry_updated_api_response()
        except Exception as e:
            return ApiResponses.simple_bad_gateway_api_response()


    # Verify API key authorization is correct for Device activities
    # Outcomes:
    #   - No authorization header -> Forbidden
    #   - Wrong authorization header -> Forbidden
    #   - Success -> Return result of callback function
    @classmethod
    def verify_authorized_device_request(this, callback_function):
        VERIFICATION_KEY:str = request.headers.get('Authorization', str).split()[1]
        if VERIFICATION_KEY != this.ESP_AUTH_KEY or VERIFICATION_KEY is None:
            return ApiResponses.simple_forbidden_request_api_response()
        return callback_function()
    
    
    # Try to query the db for a device matching mac_address
    # Outcomes:
    #   - Device not in db -> Bad request
    #   - Database throws error -> Bad gateway
    #   - Success -> Return result of callback function
    @classmethod
    def verify_mac_address_exists(this, callback_function):
        data = request.get_json()

        # Check if mac_address is in the json body
        mac_address = data.get('mac_address')
        if mac_address is None:
            return ApiResponses.simple_baq_request_api_response_with_missing_parameter("mac_address")
        
        try:
            device_exists = DatabaseFunctions.contains_device_by_mac_address(mac_address=mac_address)
            if not device_exists:
                return ApiResponses.simple_baq_request_api_response_with_data(f"mac_address \'{mac_address}\' does not exist")
            return callback_function()
        except Exception as e:
            return ApiResponses.simple_bad_gateway_api_response()
            
    # Verify API key authorization is correct for User activities
    # Outcomes:
    #   - No authorization header -> Forbidden
    #   - Wrong authorization header -> Forbidden
    #   - Success -> Return result of callback function
    @classmethod
    def verify_authorized_user_request(this, callback_function):
        VERIFICATION_KEY:str = request.headers.get('Authorization', str).split()[1]
        if VERIFICATION_KEY != this.REGISTER_USER_AUTH or VERIFICATION_KEY is None:
            return ApiResponses.simple_forbidden_request_api_response()
        return callback_function()

    # Try to get user email from body, also check if already in database
    # Outcomes:
    @classmethod
    def verify_email_given_and_not_exists(this, callback_function):
        data = request.get_json()

        email = data.get('email')
        if email is None:
            return ApiResponses.simple_baq_request_api_response_with_missing_parameter("email")
        
        try:
            email_exists = DatabaseFunctions.contains_user_email_already(email=email)
            if email_exists:
                return ApiResponses.simple_baq_request_api_response_with_data(f"email \'{email}\' already exists")
            return callback_function()
        except Exception as e:
            return ApiResponses.simple_bad_gateway_api_response()
            

    @classmethod
    def insert_new_user(this):

        data = request.get_json()
        email = data.get('email')

        try:
            DatabaseFunctions.insert_new_user_by_email(email=email)
            return ApiResponses.simple_entry_created_api_response()
        except Exception as e:
            return ApiResponses.simple_bad_gateway_api_response()