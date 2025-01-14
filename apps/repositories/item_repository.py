from typing import Dict, List
from dataclasses import replace

from ..domains import Item, ItemRepositoryInterface
from ..exceptions import (
    ItemNotFoundException, ItemAlreadyExistsException, ItemRepositoryException
)


class ItemRepository(ItemRepositoryInterface):
    def __init__(self):
        self.items: Dict[str, Item] = {}

    def create(self, item: Item) -> Dict[str, Item]:
        try:
            item_id = str(len(self.items) + 1)
            if item_id in self.items:
                raise ValueError(
                    f"Item {item_id} already exists"
                )
            self.items[item_id] = item
            return {
                item_id: item
            }
        except ValueError as e:
            raise ItemAlreadyExistsException(str(e))
        except Exception as e:
            raise ItemRepositoryException(
                f"Item {item_id} could not be created, " + str(e)
            )

    def get_by_id(self, item_id: str) -> Item:
        try:
            if item_id not in self.items:
                raise ValueError(f"Item {item_id} not found")
            result = self.items[item_id]
            return result.__dict__
        except ValueError as e:
            raise ItemNotFoundException(str(e))
        except Exception as e:
            raise ItemRepositoryException(
                f"Item {item_id} could not be retrieved, " + str(e)
            )

    def delete(self, item_id: str) -> str:
        try:
            if item_id not in self.items:
                raise ValueError(f"Item {item_id} not found")
            del self.items[item_id]
            return f"Item {item_id} removed"
        except ValueError as e:
            raise ItemNotFoundException(str(e))
        except Exception as e:
            raise ItemRepositoryException(
                f"Item {item_id} could not be deleted, " + str(e)
            )

    def get_all(self) -> List[Item]:
        try:
            return list(self.items.values())
        except Exception as e:
            raise ItemRepositoryException(
                "Error: could not retrieve items, " + str(e)
            )

    def update(self, item_id: str, data: Dict[str, str]) -> Item:
        try:
            if item_id not in self.items:
                raise ValueError(f"Item {item_id} not found")

            self.items[item_id] = replace(self.items[item_id], **data)
            return f"Item updated: {item_id}"

        except ValueError as e:
            raise ItemNotFoundException(str(e))
        except Exception as e:
            raise ItemRepositoryException(
                f"Item {item_id} could not be updated, " + str(e)
            )
