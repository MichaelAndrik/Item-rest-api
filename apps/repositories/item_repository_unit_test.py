from typing import Any, Callable

import pytest
from faker import Faker
from pytest_mock import MockFixture

from ..domains import Item
from ..repositories import ItemRepository


@pytest.fixture
def test_data_factory(faker: Faker) -> Callable[..., Any]:
    def factory(**kwargs: Any) -> Any:
        name = kwargs.get("name", faker.word())
        price = kwargs.get("price", faker.pyfloat(positive=True))
        quantity = kwargs.get("quantity", faker.random_int(min=0, max=100))
        item = Item(name=name, price=price, quantity=quantity)
        return {
            "item": item
        }

    return factory


@pytest.fixture
def dependencies(mocker: MockFixture) -> Callable[..., Any]:
    def factory(**kwargs: Any) -> Any:
        item_repository = ItemRepository()
        item_repository.create = mocker.Mock(side_effect=kwargs.get("create_response"))
        item_repository.get_by_id = mocker.Mock(side_effect=kwargs.get("get_by_id_response"))
        item_repository.delete = mocker.Mock(side_effect=kwargs.get("delete_response"))
        item_repository.get_all = mocker.Mock(side_effect=kwargs.get("get_all_response"))
        item_repository.update = mocker.Mock(side_effect=kwargs.get("update_response"))
        return {
            "item_repository": item_repository
        }

    return factory


class ItemRepositoryTest:
    def test_create_item(
        self, test_data_factory: Callable[..., Any], dependencies: Callable[..., Any]
    ) -> None:
        data = test_data_factory()
        item_id = "1"
        repository = dependencies(create_response={item_id: data["item"]})

        result = repository["item_repository"].create(data["item"])

        assert result == data["item"]

    def test_get_by_id(
        self, test_data_factory: Callable[..., Any], dependencies: Callable[..., Any]
    ) -> None:
        data = test_data_factory()
        repository = dependencies(get_by_id_response=data["item"].__dict__)

        result = repository["item_repository"].get_by_id("1")

        assert result == data["item"]

    def test_delete_item(
        self, test_data_factory: Callable[..., Any], dependencies: Callable[..., Any]
    ) -> None:
        data = test_data_factory()
        item_id = "1"
        repository = dependencies(
            create_response={item_id: data["item"]},
            delete_response="Item 1 removed"
        )

        result = repository["item_repository"].delete("1")

        assert result == "Item 1 removed"
