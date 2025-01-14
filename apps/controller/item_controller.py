from flask import Blueprint, request, jsonify
from pydantic import ValidationError

from ..domains import ItemSchema, Item
from ..use_cases import ItemUseCase
from ..repositories import ItemRepository
from ..common import StatusCode


item = Blueprint("item", __name__)
item_use_case = ItemUseCase(ItemRepository())


@item.route("/", methods=["POST"])
def create():
    item_data = ItemSchema(**request.json)
    item = Item(**item_data.dict())
    return item_use_case.create(item)


@item.route("/<item_id>", methods=["GET"])
def get_by_id(item_id: str):
    return item_use_case.get_by_id(item_id)


@item.route("/<item_id>", methods=["DELETE"])
def delete(item_id: str):
    return item_use_case.delete(item_id)


@item.route("/", methods=["GET"])
def get_all():
    return item_use_case.get_all()


@item.route("/<item_id>", methods=["PUT"])
def update(item_id: str):
    try:
        item_data = ItemSchema(**request.json)
        return item_use_case.update(item_id, item_data.dict())
    except ValidationError as e:
        return jsonify({
            "error": "Validation Error",
            "detail": e.errors()
        }), StatusCode.BAD_REQUEST
