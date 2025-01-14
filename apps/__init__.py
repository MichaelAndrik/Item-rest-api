import inspect
from flask import Flask, Blueprint

from .controller.handler_exception import register_error_handlers


def run_app():
    app = Flask(__name__)

    register_blueprints(app)
    register_error_handlers(app)

    return app


def register_blueprints(flask_app):
    from apps import controller
    blueprints = inspect.getmembers(
        controller, lambda member: isinstance(member, Blueprint)
    )

    for name, blueprint in blueprints:
        prefix = f'/api/{name.replace("_", "-")}' if name != 'index' else '/api' # noqa
        flask_app.register_blueprint(blueprint, url_prefix=prefix)
