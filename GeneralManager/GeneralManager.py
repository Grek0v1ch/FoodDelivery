import json
import random

from DeliveryManager.DeliveryManager import DeliveryManager
from DeliveryManager.DeliveryMan import DeliveryMan
from GroceryRetailer.GroceryRetailerManager import GroceryRetailerManager
from System import System
from MetaSingleton import MetaSingleton


class GeneralManager(metaclass=MetaSingleton):
    def __init__(self):
        self.__delivery_manager: DeliveryManager = DeliveryManager()
        self.__grocery_manager: GroceryRetailerManager = \
            GroceryRetailerManager()
        self.__load_retailers('resources/GroceryRetailers.json')
        self.__load_delivery_mans('DeliveryMans.json')

    def __load_retailers(self, file_path: str) -> None:
        self.__grocery_manager.load_json(file_path)

    def __load_delivery_mans(self, file_path: str) -> None:
        with open(file_path, 'r') as f:
            text = json.load(f)
        for i in range(len(text)):
            man = DeliveryMan(text[i]["area"], text[i]["current_order"],
                              text[i]["transport"],
                              text[i]["order_time"], text[i]["time_start"])
            self.__delivery_manager.add_deliveryman(man)

    def __get_order_status_str(self) -> str:
        result = []
        order_status = self.__delivery_manager.get_orders_status()
        for status in order_status[0]:
            result.append(f'Заказ {status} выполнен!')
        for status in order_status[1]:
            result.append(f'Оставшееся время доставки заказа {status[0]}: '
                          f'{status[1]}')
        return '\n'.join(result)

    def start(self):
        while True:
            print('Меню:',
                  '1. Сделать новый заказ',
                  '2. Уточнить статус заказов', sep='\n')
            chose = System.validate_integer_in_range(1, 2)
            System.clear_terminal()
            if chose == 1:
                order = self.__grocery_manager.make_order()
                if order.is_valid_order:
                    print('Заказ принят. Ищем доставщика...')
                    length = random.randint(0, 3000)
                    if self.__delivery_manager.accept_order(
                            order,
                            length
                    ) is None:
                        print('Свободных доставщиков в вашем районе пока нет, '
                              'идет поиск...')
                        while self.__delivery_manager.accept_order(
                                order,
                                length
                        ) is None:
                            print(self.__get_order_status_str())
                            time.sleep(5)
                            delivery_manager.tick()
                    print('Доставщик найден! Вам доставит еду Матвей')
                    _ = input()
                    System.clear_terminal()
            elif chose == 2:
                print(self.__get_order_status_str())
                _ = input()
                System.clear_terminal()
            self.__delivery_manager.tick()
