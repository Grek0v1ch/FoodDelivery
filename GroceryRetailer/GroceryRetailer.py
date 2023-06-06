from random import randint

from CreatorID import CreatorID
from GroceryRetailer.GroceryRetailerType import GroceryRetailerType
from Order.Product import Product


class GroceryRetailer:
    """Класс продуктового ритейлера (магазина или ресторана)"""
    def __init__(
            self, name: str,
            grocery_retailer_type: GroceryRetailerType,
            menu: list[Product],
            stop_list: list[Product],
            area: int
    ):
        self.__id: tuple[str] = CreatorID.generate_grocery_retailer_id()
        self.__name: str = name
        self.__grocery_retailer_type: GroceryRetailerType = \
            grocery_retailer_type
        self.__menu: list[Product] = menu
        self.__stop_list: list[Product] = stop_list
        self.__area: int = area

    def __str__(self):
        return f'Имя: {self.__name}, Тип: {self.__grocery_retailer_type}, ' \
               f'Меню: {[str(item) for item in self.__menu]}, ' \
               f'Стоп лист: {self.__stop_list}'

    @property
    def name(self) -> str:
        return self.__name

    @property
    def id(self) -> tuple[str]:
        return self.__id

    @property
    def menu(self) -> list[Product]:
        return self.__menu

    @property
    def stop_list(self) -> list[Product]:
        return self.__stop_list

    @property
    def area(self) -> int:
        return self.__area

    def updating_menu(self):
        """ Метод обновляет меню"""
        # Обновление меню происходит рандомно: сначала выбираем какой продукт
        # вернуть в меню, потом удаляем что-то из меню, и возвращаем в меню
        # выбранный в начале продукт
        temp = randint(0, 1)
        selected_product_stop_list = None
        # убираем из стоп листа
        if temp == 1:
            if len(self.__stop_list) != 0:
                selected_product_stop_list = self.__stop_list[
                    randint(0, len(self.__stop_list) - 1)]
                self.__stop_list.remove(selected_product_stop_list)
        temp = randint(0, 1)
        # убираем из меню
        if temp == 1 and len(self.__stop_list) < len(self.__menu):
            if len(self.__menu) != 0:
                selected_product_menu = self.__menu[
                    randint(0, len(self.__menu) - 1)]
                self.__stop_list.append(selected_product_menu)
                self.__menu.remove(selected_product_menu)
        # возвращаем в меню
        if selected_product_stop_list is not None:
            self.__menu.append(selected_product_stop_list)
        return self.__menu
