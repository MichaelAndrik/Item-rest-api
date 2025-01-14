from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import List, Dict
from pydantic import BaseModel, field_validator


@dataclass(frozen=True)
class Item:
    name: str
    price: float
    quantity: int = 0


class ItemSchema(BaseModel):
    name: str
    price: float
    quantity: int

    @field_validator("name")
    def validate_name(cls, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        if len(value) == 0:
            raise ValueError("Name cannot be empty")
        return value

    @staticmethod
    def validate_positive_number(value):
        if isinstance(value, str):
            raise ValueError("Price must be a number, not a string")
        if value <= 0:
            raise ValueError("Price must be positive number")
        return value

    @field_validator("price")
    def validate_price(cls, value):
        return cls.validate_positive_number(value)

    @field_validator("quantity")
    def validate_quantity(cls, value):
        return cls.validate_positive_number(value)


class ItemRepositoryInterface(ABC):
    @abstractmethod
    def get_all(self) -> List[Item]:
        pass

    @abstractmethod
    def get_by_id(self, item_id: int) -> Item:
        pass

    @abstractmethod
    def create(self, item: Item) -> Dict[int, Item]:
        pass

    @abstractmethod
    def update(self, item_id: int, data: Dict[str, str]) -> Item:
        pass

    @abstractmethod
    def delete(self, item_id: int) -> Item:
        pass
