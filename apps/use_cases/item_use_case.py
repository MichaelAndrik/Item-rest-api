from ..repositories import ItemRepository
from ..domains import Item


class ItemUseCase:
    def __init__(self, item_repository: ItemRepository):
        self.item_repository = item_repository

    def create(self, item: Item):
        return self.item_repository.create(item)

    def get_by_id(self, item_id: str):
        return self.item_repository.get_by_id(item_id)

    def delete(self, item_id: str):
        return self.item_repository.delete(item_id)

    def get_all(self):
        return self.item_repository.get_all()

    def update(self, item_id: str, data: dict):
        return self.item_repository.update(item_id, data)
