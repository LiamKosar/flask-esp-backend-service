from flask import jsonify

# Makes API Responses easier
class ApiResponses:

    # Class-level dictionary holding response data
    RESPONSE_DATA = {
        "BAD_REQUEST": "Bad Request",
        "BAD_REQUEST_CODE": 400,
        "FORBIDDEN": "Forbidden",
        "FORBIDDEN_CODE": 403,
        "UNAUTHORIZED": "Unauthorized",
        "UNAUTHORIZED_CODE": 401,
        "ENTRY_CREATED": "Entry Created",
        "SUCCESSFUL_ENTRY_CREATED_CODE": 201,
        "ENTRY_DELETED": "Entry Deleted",
        "SUCCESSFUL_ENTRY_DELETED_CODE": 200,
        "ENTRY_UPDATED": "Entry Updated",
        "SUCCESSFUL_ENTRY_UPDATED_CODE": 200,
        "BAD_GATEWAY": "Bad Gateway",
        "BAD_GATEWAY_CODE": 502,
        "SUCCESS_MSG": "Success",
        "SUCCESSFUL_ENTRY_GET_CODE": 200,
        "SUCCESSFULL_CONNECTION": "Connected",
        "SUCCESSFULL_CONNECTION_CODE": 200,
    }

    @classmethod
    def simple_api_response(this, message: str, data: str, status: int):
        return jsonify({"message": message, "data": data}), status
    
    @classmethod
    def simple_device_connected_api_response(this):
        return jsonify({"message": this.RESPONSE_DATA["SUCCESSFULL_CONNECTION"]}), this.RESPONSE_DATA["SUCCESSFULL_CONNECTION_CODE"]

    @classmethod
    def simple_baq_request_api_response(this):
        return jsonify({"message": this.RESPONSE_DATA["BAD_REQUEST"]}), this.RESPONSE_DATA["BAD_REQUEST_CODE"]
    
    @classmethod
    def simple_baq_request_api_response_with_data(this, data: str):
        return jsonify({"message": data}), this.RESPONSE_DATA["BAD_REQUEST_CODE"]
    
    @classmethod
    def simple_baq_request_api_response_with_missing_parameter(this, parameter: str):
        return jsonify({"message": f"Body parameter \'{parameter}\' is missing"}), this.RESPONSE_DATA["BAD_REQUEST_CODE"]

    @classmethod
    def simple_forbidden_request_api_response(this):
        return jsonify({"message": this.RESPONSE_DATA["FORBIDDEN"]}), this.RESPONSE_DATA["FORBIDDEN_CODE"]

    @classmethod
    def simple_unauthorized_request_api_response(this):
        return jsonify({"message": this.RESPONSE_DATA["UNAUTHORIZED"]}), this.RESPONSE_DATA["UNAUTHORIZED_CODE"]

    @classmethod
    def simple_entry_created_api_response(this):
        return jsonify({"message": this.RESPONSE_DATA["ENTRY_CREATED"]}), this.RESPONSE_DATA["SUCCESSFUL_ENTRY_CREATED_CODE"]

    @classmethod
    def simple_entry_deleted_api_response(this):
        return jsonify({"message": this.RESPONSE_DATA["ENTRY_DELETED"]}), this.RESPONSE_DATA["SUCCESSFUL_ENTRY_DELETED_CODE"]

    @classmethod
    def simple_entry_updated_api_response(this):
        return jsonify({"message": this.RESPONSE_DATA["ENTRY_UPDATED"]}), this.RESPONSE_DATA["SUCCESSFUL_ENTRY_UPDATED_CODE"]

    @classmethod
    def simple_bad_gateway_api_response(this):
        return jsonify({"message": this.RESPONSE_DATA["BAD_GATEWAY"]}), this.RESPONSE_DATA["BAD_GATEWAY_CODE"]

    @classmethod
    def simple_get_api_response(this, data: str):
        return jsonify({"message": this.RESPONSE_DATA["SUCCESS_MSG"], "data": data}), this.RESPONSE_DATA["SUCCESSFUL_ENTRY_GET_CODE"]
