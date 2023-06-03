import json
import random
import time

from DeliveryManager.DeliveryMan import DeliveryMan
from DeliveryManager.DeliveryManager import DeliveryManager
from GroceryRetailer.GroceryRetailerManager import GroceryRetailerManager
from System import System


def main():
    manager = GroceryRetailerManager()
    manager.load_json('resources/GroceryRetailers.json')
    delivery_manager = DeliveryManager()
    with open('DeliveryMans.json', 'r') as f:
        text = json.load(f)

    for i in range(len(text)):
        man = DeliveryMan(text[i]["area"], text[i]["current_order"],
                          text[i]["transport"],
                          text[i]["order_time"], text[i]["time_start"])
        delivery_manager.add_deliveryman(man)
    while True:
        print('Меню:',
              '1. Сделать новый заказ',
              '2. Уточнить статус заказов', sep='\n')
        chose = System.validate_integer_in_range(1, 2)
        System.clear_terminal()
        if chose == 1:
            order = manager.make_order()
            length = random.randint(0, 3000)
            if delivery_manager.accept_order(order, length) is None:
                print('Свободных доставщиков в вашем районе пока нет, '
                      'идет поиск...')
                while delivery_manager.accept_order(order, length) is None:
                    print(delivery_manager.get_order_status(order))
                    time.sleep(5)
                    delivery_manager.tick()
            # Debug
            print(delivery_manager.get_order_status(order))
        elif chose == 2:
            print(delivery_manager.get_order_status(order))
            _ = input()
            System.clear_terminal()
        delivery_manager.tick()


if __name__ == "__main__":
    main()
