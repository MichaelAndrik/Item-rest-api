from flask import Blueprint

api = Blueprint("api", __name__)


@api.route("/", methods=["GET"])
def index():
    return 'App is running!', 200


@api.route("/hello", methods=["GET"])
def hello():
    return "Hello, World!", 200
