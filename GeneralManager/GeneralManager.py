import json
import random
import time

from CreatorID import CreatorID
from DeliveryManager.DeliveryManager import DeliveryManager
from DeliveryManager.DeliveryMan import DeliveryMan
from GroceryRetailer.GroceryRetailerManager import GroceryRetailerManager
from System import System
from CreatorID import CreatorID
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
            man = DeliveryMan(
                CreatorID.generate_deliveryman_id(),
                text[i]["area"],
                text[i]["current_order"],
                text[i]["transport"],
                text[i]["order_time"],
                text[i]["order_id"],
                text[i]["time_start"]
            )
            self.__delivery_manager.add_deliveryman(man)

    def __get_order_status_str(self) -> str:
        result = []
        order_status = self.__delivery_manager.get_orders_status()
        for status in order_status[0]:
            result.append(f'Заказ {status[0]} выполнен доставщиком'
                          f' {status[1]}!')
        for status in order_status[1]:
            result.append(f'Оставшееся время доставки заказа {status[0][0]}'
                          f': {status[1]}\n'
                          f'Доставщик {status[0][1]}')
        return '\n'.join(result)

    def start(self):
        while True:
            print('Меню:',
                  '1. Сделать новый заказ',
                  '2. Уточнить статус заказов',
                  '3. Выйти', sep='\n')
            chose = System.validate_integer_in_range(1, 3)
            System.clear_terminal()
            if chose == 1:
                order = self.__grocery_manager.make_order()
                if order.is_valid_order:
                    print(f'Заказ принят. Id заказа {order.id[0][-8:]}.\n'
                          f'Ищем доставщика...')
                    length = random.randint(0, 1000)
                    if not self.__delivery_manager.accept_order(
                            order,
                            length
                    ):
                        print('Свободных доставщиков в вашем районе пока нет, '
                              'идет поиск...')
                        while not self.__delivery_manager.accept_order(
                                order,
                                length
                        ):
                            print(self.__get_order_status_str())
                            time.sleep(5)
                            self.__delivery_manager.tick()
                    print('Доставщик найден!')
                    _ = input()
                    System.clear_terminal()
            elif chose == 2:
                print(self.__get_order_status_str())
                _ = input()
                System.clear_terminal()
            elif chose == 3:
                return
            self.__delivery_manager.tick()
