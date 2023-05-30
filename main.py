import json

from DeliveryMan import DeliveryMan, TransportType
from DeliveryManager import DeliveryManager
from Order import Order

manager = DeliveryManager()


with open('DeliveryMans.json', 'r') as f:
    text = json.load(f)

for i in range(len(text)):
    man = DeliveryMan(text[i]["area"], text[i]["current_order"], text[i]["transport"],
                      text[i]["order_time"], text[i]["time_start"])
    manager.add_deliveryman(man)
manager.find_deliveryman(1, 0.1)
manager.find_deliveryman(1, 0.1)
manager.find_deliveryman(1, 0.1)
manager.find_deliveryman(1, 0.1)
while True:
    manager.tick()


