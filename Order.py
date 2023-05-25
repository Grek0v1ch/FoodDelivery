from dataclasses import dataclass
from typing import Optional
from Product import Product


@dataclass
class Order:
    __id: tuple[str]
    grocery_retailer_id: Optional[tuple[str]] = None
    area: Optional[int] = None
    current_product: Optional[Product] = None  # Product
    time_cooking: Optional[int] = None
    price: Optional[float] = None

    @property
    def id(self) -> tuple[str]:
        return self.__id
