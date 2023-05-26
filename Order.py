from dataclasses import dataclass
from typing import Optional
from Product import Product


@dataclass
class Order:
    __id: tuple[str]
    grocery_retailer_id: Optional[tuple[str]] = None
    area: Optional[int] = None
    current_product: Optional[Product] = None
    time_cooking: Optional[int] = None
    price: Optional[float] = None

    @property
    def id(self) -> tuple[str]:
        return self.__id

    @property
    def is_any_none(self) -> bool:
        return self.grocery_retailer_id is None or self.area is None or \
               self.current_product is None or self.time_cooking is None or\
               self.price is None
