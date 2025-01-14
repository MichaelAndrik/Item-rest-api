from flask import Blueprint

index = Blueprint("api", __name__)


@index.route("/", methods=["GET"])
def main():
    return 'App is running!', 200
