from dataclasses import dataclass
from typing import Optional
from Order.Product import Product


@dataclass
class Order:
    __id: tuple[str]
    grocery_retailer_id: Optional[tuple[str]] = None
    area: Optional[int] = None
    products: Optional[list[Product]] = None
    weight: Optional[int] = None
    ime_cooking: Optional[int] = None
    price: Optional[float] = None

    @property
    def get_products_name(self) -> str:
        result = []
        for product in self.products:
            result.append(product.name)
        return ', '.join(result)

    @property
    def id(self) -> tuple[str]:
        return self.__id

    @property
    def is_any_none(self) -> bool:
        return self.grocery_retailer_id is None or self.area is None or \
               self.products is None or self.time_cooking is None or\
               self.price is None

    @property
    def is_valid_order(self) -> bool:
        return not self.is_any_none and len(self.products) != 0
