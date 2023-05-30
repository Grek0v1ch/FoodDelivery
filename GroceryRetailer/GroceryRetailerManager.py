import json
from typing import Optional

from GroceryRetailer.GroceryRetailer import GroceryRetailer
from Order.Order import Order
from Order.OrderBuilder import OrderBuilder
from Order.Product import Product
from System import System


class GroceryRetailerManager:
    def __init__(self):
        self.__retailers: list[GroceryRetailer] = []

    def __str__(self):
        return f'Список магазинов:\n' + '\n'.join(
            [str(item) for item in self.__retailers])

    def add_grocery_retailer(self, retailer: GroceryRetailer):
        self.__retailers.append(retailer)

    def load_json(self, file_path: str):
        with open(file_path, 'r') as file:
            data = json.load(file)
        for retailer in data:
            self.add_grocery_retailer(
                GroceryRetailer(
                    retailer['name'],
                    retailer['type'],
                    self.__load_product_list(retailer['menu']),
                    self.__load_product_list(retailer['stop_list']),
                    retailer['area']
                )
            )

    def make_order(self) -> Order:
        self.__update_retailers()
        builder = OrderBuilder()
        retailer_idx = self.__retailer_selection_menu()
        System.clear_terminal()
        while retailer_idx is not None:
            builder.add_grocery_retailer(self.__retailers[retailer_idx])
            product_idx = self.__product_selection_menu(retailer_idx)
            System.clear_terminal()
            while product_idx is not None:
                builder.add_product(
                    self.__retailers[retailer_idx].menu[product_idx]
                )
                print('Хотите выбрать что то еще?',
                      '1. Да',
                      '2. Нет', sep='\n')
                chose = System.validate_integer_in_range(1, 2)
                System.clear_terminal()
                if chose == 1:
                    product_idx = self.__product_selection_menu(retailer_idx)
                    System.clear_terminal()
                else:
                    product_idx = None
            retailer_idx = self.__retailer_selection_menu()
            System.clear_terminal()
        print('Заказ принят')
        return builder.order

    def __retailer_selection_menu(self) -> Optional[int]:
        retailers_name = self.__get_retailers_name_list()
        print(f'Выберите что вас интересует',
              retailers_name,
              f'0. Назад', sep='\n')
        chose = System.validate_integer_in_range(0, len(self.__retailers))
        if chose != 0:
            return chose - 1
        else:
            return None

    def __product_selection_menu(self, retailer_idx: int):
        print('Меню заведения: ',
              self.__get_retailers_menu(retailer_idx),
              f'{len(self.__retailers[retailer_idx].menu) + 1}. Назад',
              sep='\n')
        print('Выберите номер')
        chose = System.validate_integer_in_range(
            1,
            len(self.__retailers[retailer_idx].menu) + 1
        )
        System.clear_terminal()
        if chose < len(self.__retailers[retailer_idx].menu) + 1:
            return chose - 1
        else:
            return None

    def __update_retailers(self):
        for retailer in self.__retailers:
            retailer.updating_menu()

    def __get_retailers_name_list(self) -> str:
        result = []
        for number, retailer in enumerate(self.__retailers):
            result.append(f'{number + 1}. {retailer.name}')
        return '\n'.join(result)

    def __get_retailers_menu(self, idx: int) -> str:
        result = []
        for number, product in enumerate(self.__retailers[idx].menu):
            result.append(f'{number + 1}. {product}')
        return '\n'.join(result)

    @staticmethod
    def __load_product_list(data: list[dict]) -> list[Product]:
        result: list[Product] = []
        for product in data:
            result.append(
                Product(
                    name=product['name'],
                    price=product['price'],
                    weight=product['weight'],
                    composition=product['composition']
                )
            )
        return result
