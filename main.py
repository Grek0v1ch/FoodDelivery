import json

from DelivaryMan import DelivaryMan, TransportType
from DelivaryManager import DelivaryManager


manager = DelivaryManager()


with open('DelivaryMans.json', 'r') as f:
    text = json.load(f)

man = DelivaryMan(text["area"], text["current_order"], text["transport"],
                  text["order_time"], text["time_start"])
manager.add_delivaryman(man)
manager.process_order(1, 0.1)
while man.current_order:
    man.tick()
print('Yes')
manager.tick()
manager.process_order(1, 0.5)
while man.current_order:
    man.tick()
print('Yes')
