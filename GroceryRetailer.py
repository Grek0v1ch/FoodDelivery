from CreatorID import CreatorID
from GroceryRetailerType import GroceryRetailerType
from Product import Product


class GroceryRetailer:
    def __init__(
            self, name: str,
            grocery_retailer_type: GroceryRetailerType,
            menu: list[Product],
            stop_list: list[Product]
    ):
        self.__id: tuple[str] = CreatorID.generate_grocery_retailer_id()
        self.__name: str = name
        self.__grocery_retailer_type: GroceryRetailerType = \
            grocery_retailer_type
        self.__menu: list[Product] = menu
        self.__stop_list: list[Product] = stop_list

    def __str__(self):
        return f'Имя: {self.__name}, Тип: {self.__grocery_retailer_type}, ' \
               f'Меню: {self.__menu}, Стоп лист: {self.__stop_list}'
