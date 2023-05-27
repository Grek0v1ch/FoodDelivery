import json

from DelivaryMan import DelivaryMan, TransportType
from DelivaryManager import DelivaryManager
from Order import Order

manager = DelivaryManager()


with open('DelivaryMans.json', 'r') as f:
    text = json.load(f)

for i in range(len(text)):
    man = DelivaryMan(text[i]["area"], text[i]["current_order"], text[i]["transport"],
                      text[i]["order_time"], text[i]["time_start"])
    manager.add_delivaryman(man)
manager.process_order(1, 0.1)
manager.process_order(1, 0.1)
manager.process_order(1, 0.1)
manager.process_order(1, 0.1)
while True:
    manager.tick()


