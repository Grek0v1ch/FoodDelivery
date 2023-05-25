import json
import os

from GroceryRetailer import GroceryRetailer
from Order import Order
from OrderBuilder import OrderBuilder
from Product import Product


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
        builder = OrderBuilder()
        print('Выберите магазин:',
              self.__get_retailers_name_list(), sep='\n')
        # TODO: Нужно написать метод ввода целого числа в диапазоне [a, b]
        number_retailer = int(input('Введите номер магазина: '))
        os.system('clear')
        builder.add_grocery_retailer(self.__retailers[number_retailer - 1].id)
        print('Меню магазина: ',
              self.__get_retailers_menu(number_retailer - 1), sep='\n')
        number_product = int(input('Введите номер продукта: '))
        builder.add_product(
            self.__retailers[number_retailer - 1].menu[number_product - 1]
        )
        builder.add_area(self.__retailers[number_retailer - 1].area)
        # TODO: Сделать время готовки
        builder.add_time_cooking(10)
        builder.add_price(
            self.__retailers[number_retailer - 1].menu[number_product - 1].price
        )
        return builder.order

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
