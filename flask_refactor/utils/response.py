from flask import jsonify

def success_response(message="", data=None, status_code=200, pagination=None):

    response = {
        "status": "success",
        "message": message,
        "data": data
    }

    if pagination:
        response["pagination"] = pagination

    return jsonify(response), status_code


def error_response(message="Error", status_code=500, data=None):
    return jsonify({
        "status": "error",
        "message": message,
        "data": data
    }), status_code