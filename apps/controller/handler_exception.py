
from flask import Flask, jsonify
from pydantic import ValidationError

from ..exceptions import ItemException
from ..common import StatusCode


def register_error_handlers(app: Flask):
    @app.errorhandler(ItemException)
    def handle_item_exception(error: ItemException):
        response = jsonify({
            "error": error.message,
            "status_code": error.status_code
        }), error.status_code
        return response

    @app.errorhandler(Exception)
    def handler_general_exception(error: Exception):
        return jsonify({
            "error": str(error),
            "status_code": StatusCode.INTERNAL_SERVER_ERROR
        }), StatusCode.INTERNAL_SERVER_ERROR

    @app.errorhandler(ValidationError)
    def handle_validation_error(error: ValidationError):
        errors = [
            f"Field {err['loc'][-1]}: {err['msg']}" for err in error.errors()
        ]
        return jsonify({
            "error": "Validation Error",
            "detail": errors
        }), StatusCode.BAD_REQUEST
