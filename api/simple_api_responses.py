from flask import jsonify

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
    def simple_api_response(cls, message: str, data: str, status: int):
        return jsonify({"message": message, "data": data}), status
    
    @classmethod
    def simple_device_connected_api_response(cls):
        return jsonify({"message": cls.RESPONSE_DATA["SUCCESSFULL_CONNECTION"]}), cls.RESPONSE_DATA["SUCCESSFULL_CONNECTION_CODE"]

    @classmethod
    def simple_baq_request_api_response(cls):
        return jsonify({"message": cls.RESPONSE_DATA["BAD_REQUEST"]}), cls.RESPONSE_DATA["BAD_REQUEST_CODE"]
    
    @classmethod
    def simple_baq_request_api_response_with_data(cls, data: str):
        return jsonify({"message": data}), cls.RESPONSE_DATA["BAD_REQUEST_CODE"]
    
    @classmethod
    def simple_baq_request_api_response_with_missing_parameter(cls, parameter: str):
        return jsonify({"message": f"Body parameter \'{parameter}\' is missing"}), cls.RESPONSE_DATA["BAD_REQUEST_CODE"]

    @classmethod
    def simple_forbidden_request_api_response(cls):
        return jsonify({"message": cls.RESPONSE_DATA["FORBIDDEN"]}), cls.RESPONSE_DATA["FORBIDDEN_CODE"]

    @classmethod
    def simple_unauthorized_request_api_response(cls):
        return jsonify({"message": cls.RESPONSE_DATA["UNAUTHORIZED"]}), cls.RESPONSE_DATA["UNAUTHORIZED_CODE"]

    @classmethod
    def simple_entry_created_api_response(cls):
        return jsonify({"message": cls.RESPONSE_DATA["ENTRY_CREATED"]}), cls.RESPONSE_DATA["SUCCESSFUL_ENTRY_CREATED_CODE"]

    @classmethod
    def simple_entry_deleted_api_response(cls):
        return jsonify({"message": cls.RESPONSE_DATA["ENTRY_DELETED"]}), cls.RESPONSE_DATA["SUCCESSFUL_ENTRY_DELETED_CODE"]

    @classmethod
    def simple_entry_updated_api_response(cls):
        return jsonify({"message": cls.RESPONSE_DATA["ENTRY_UPDATED"]}), cls.RESPONSE_DATA["SUCCESSFUL_ENTRY_UPDATED_CODE"]

    @classmethod
    def simple_bad_gateway_api_response(cls):
        return jsonify({"message": cls.RESPONSE_DATA["BAD_GATEWAY"]}), cls.RESPONSE_DATA["BAD_GATEWAY_CODE"]

    @classmethod
    def simple_get_api_response(cls, data: str):
        return jsonify({"message": cls.RESPONSE_DATA["SUCCESS_MSG"], "data": data}), cls.RESPONSE_DATA["SUCCESSFUL_ENTRY_GET_CODE"]
