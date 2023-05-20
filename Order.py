from dataclasses import dataclass
from typing import Optional


@dataclass
class Order:
    __id: int
    grocery_retailer_id: Optional[int] = None
    area: Optional[int] = None
    current_product: Optional[bool] = None  # Product
    time_cooking: Optional[int] = None
    price: Optional[float] = None

    @property
    def id(self) -> int:
        return self.__id
