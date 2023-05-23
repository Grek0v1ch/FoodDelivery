from typing import Optional, Union

from Area import Area
from DelivaryMan import DelivaryMan
from MetaSingleton import MetaSingleton
from Order import Order


class DelivaryManager(metaclass=MetaSingleton):
    def __init__(self):
        self.areas: Optional[list[Area]] = []
        self.__orders_queue: list[int] = []

    def add_delivaryman(self, deliveryman: DelivaryMan) -> None:
        self.areas[deliveryman.area].add_delivaryman(deliveryman)

    def tick(self) -> None:
        for area in self.areas:
            area.tick()

    def process_order(self, order: Order, road_length: float) -> Union[DelivaryMan, bool]:
        self.tick()
        deliveryman = self.areas[Order.area].find_delivaryman(road_length)
        if Order.area != 0 and not isinstance(deliveryman, DelivaryMan):
            deliveryman = self.areas[Order.area - 1].find_delivaryman(3000)
        if Order.area != len(self.areas) - 1 and not isinstance(deliveryman, DelivaryMan):
            deliveryman = self.areas[Order.area + 1].find_delivaryman(3000)
        if isinstance(deliveryman, DelivaryMan):
            deliveryman.current_order = order
            deliveryman.timer_start(road_length)
        return deliveryman


