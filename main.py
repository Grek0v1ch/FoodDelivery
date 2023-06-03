import json
import random
import time

from DeliveryManager.DeliveryMan import DeliveryMan
from DeliveryManager.DeliveryManager import DeliveryManager
from GroceryRetailer.GroceryRetailerManager import GroceryRetailerManager


def main():
    manager = GroceryRetailerManager()
    manager.load_json('resources/GroceryRetailers.json')
    order = manager.make_order()
    delivery_manager = DeliveryManager()
    with open('DeliveryMans.json', 'r') as f:
        text = json.load(f)

    for i in range(len(text)):
        man = DeliveryMan(text[i]["area"], text[i]["current_order"],
                          text[i]["transport"],
                          text[i]["order_time"], text[i]["time_start"])
        delivery_manager.add_deliveryman(man)
    delivery_manager.accept_order(order, random.randint(0, 3000))
    while True:
        print(delivery_manager.get_order_status(order))
        delivery_manager.tick()
        time.sleep(5)


if __name__ == "__main__":
    main()
