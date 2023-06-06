import json
from typing import Optional

from GroceryRetailer.GroceryRetailer import GroceryRetailer
from Order.Order import Order
from Order.OrderBuilder import OrderBuilder
from Order.Product import Product
from System import System
from MetaSingleton import MetaSingleton


class GroceryRetailerManager(metaclass=MetaSingleton):
    """Класс-менеджер магазинов и ресторанов"""
    def __init__(self):
        self.__retailers: list[GroceryRetailer] = []

    def __str__(self):
        return f'Список магазинов:\n' + '\n'.join(
            [str(item) for item in self.__retailers])

    def add_grocery_retailer(self, retailer: GroceryRetailer):
        """Метод добавляет новый магазин или ресторан в менеджер"""
        self.__retailers.append(retailer)

    def load_json(self, file_path: str):
        """Метод загружает информацию о магазинах из файла .json"""
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

    @staticmethod
    def __load_product_list(data: list[dict]) -> list[Product]:
        """Метод загружает список продуктов"""
        result: list[Product] = []
        for product in data:
            result.append(
                Product(
                    name=product['name'],
                    price=product['price'],
                    weight=product['weight'],
                    composition=product['composition'],
                    time_cooking=product['time_cooking']
                )
            )
        return result

    def make_order(self) -> Order:
        """
        Метод формирует заказ. Взаимодействие с пользователем осуществляется
        через консоль
        """
        self.__update_retailers()
        builder = OrderBuilder()
        retailer_idx = self.__retailer_selection_menu()
        System.clear_terminal()
        while retailer_idx is not None:
            builder.add_grocery_retailer(self.__retailers[retailer_idx])
            product_idx = self.__product_selection_menu(retailer_idx)
            System.clear_terminal()
            while product_idx is not None:
                if product_idx == -1:
                    print('Ваша корзина: ',
                          builder.order.get_products_name, sep='\n')
                else:
                    builder.add_product(
                        self.__retailers[retailer_idx].menu[product_idx]
                    )
                print('Хотите выбрать что то еще?',
                      '1. Да',
                      '2. Нет, завершить сборку заказа', sep='\n')
                chose = System.validate_integer_in_range(1, 2)
                System.clear_terminal()
                if chose == 1:
                    product_idx = self.__product_selection_menu(retailer_idx)
                    System.clear_terminal()
                elif chose == 2:
                    return builder.order
                if product_idx is None:
                    print('Если вы выберите другое заведение, то текущий заказ '
                          'сбросится. Вы точно хотите это сделать?',
                          '1. Да',
                          '2. Нет, вернуться в меню заведения', sep='\n')
                    chose = System.validate_integer_in_range(1, 2)
                    System.clear_terminal()
                    if chose == 2:
                        product_idx = self.__product_selection_menu(
                            retailer_idx
                        )
            retailer_idx = self.__retailer_selection_menu()
            System.clear_terminal()
        return builder.order

    def __retailer_selection_menu(self) -> Optional[int]:
        """
        Метод выводит меню выбора магазина или ресторана и принимает ответ
        пользователя
        """
        retailers_name = self.__get_retailers_name_list()
        print(f'Выберите заведение, из которого будет оформлен заказ',
              retailers_name,
              f'0. Назад', sep='\n')
        chose = System.validate_integer_in_range(0, len(self.__retailers))
        if chose != 0:
            return chose - 1
        else:
            return None

    def __product_selection_menu(self, retailer_idx: int) -> Optional[int]:
        """
        Метод выводит меню выбора позиций в магазине или ресторане и принимает
        ответ пользователя
        """
        print('Меню заведения: ',
              '0. Перейти в корзину',
              self.__get_retailers_menu(retailer_idx),
              f'{len(self.__retailers[retailer_idx].menu) + 1}. Назад',
              sep='\n')
        print('Выберите номер')
        chose = System.validate_integer_in_range(
            0,
            len(self.__retailers[retailer_idx].menu) + 1
        )
        System.clear_terminal()
        if chose < len(self.__retailers[retailer_idx].menu) + 1:
            return chose - 1
        else:
            return None

    def __update_retailers(self):
        """Метод обновляет меню во всех магазинах и ресторанах"""
        for retailer in self.__retailers:
            retailer.updating_menu()

    def __get_retailers_name_list(self) -> str:
        """Метод формирует список всех ресторанов и магазинов в виде строки"""
        result = []
        for number, retailer in enumerate(self.__retailers):
            result.append(f'{number + 1}. {retailer.name}')
        return '\n'.join(result)

    def __get_retailers_menu(self, idx: int) -> str:
        """
        Метод формирует список всех позиций в магазине или ресторане в виде
        строки
        """
        result = []
        for number, product in enumerate(self.__retailers[idx].menu):
            result.append(f'{number + 1}. {product}')
        return '\n'.join(result)
