from dataclasses import dataclass
from typing import Optional

from Order.Product import Product


@dataclass
class Order:
    """
    Класс для представления заказа.

    Атрибуты:
    grocery_retailer_id : str
        id магазина или ресторана для заказа
    area : int
        район
    products : list
        составляющие заказа
    weight : int
        вес заказа
    time_cooking : int
        время приготовления заказа
    price : int
        стоимость заказа
    """
    __id: tuple[str]
    grocery_retailer_id: Optional[tuple[str]] = None
    area: Optional[int] = None
    products: Optional[list[Product]] = None
    weight: Optional[int] = None
    time_cooking: Optional[int] = None
    price: Optional[float] = None

    @property
    def get_products_name(self) -> str:
        """
        Возвращает составляющие заказа через запятую.
        """
        result = []
        for product in self.products:
            result.append(product.name)
        return ', '.join(result)

    @property
    def id(self) -> tuple[str]:
        return self.__id

    @property
    def is_any_none(self) -> bool:
        """
        Проверяет есть ли какое-либо поле, равное None.

        Возвращаемое значение:
        True, если хотя бы одно поле равно none.
        False в противном случае.
        """
        return self.grocery_retailer_id is None or self.area is None or \
            self.products is None or self.time_cooking is None or \
            self.price is None

    @property
    def is_valid_order(self) -> bool:
        """
        Проверяет, что заказ валидный.
        Заказ валидный, если в нем нет полей со значением None
        и если список продуктов в нем не пустой.

        Возвращаемое значение:
        True, если заказ валидный.
        False в противном случае.
        """
        return not self.is_any_none and len(self.products) != 0
