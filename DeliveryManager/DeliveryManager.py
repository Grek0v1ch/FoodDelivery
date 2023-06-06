import random
from typing import Optional

from DeliveryManager.DeliveryMan import DeliveryMan
from DeliveryManager.Area import Area
from MetaSingleton import MetaSingleton
from Order.Order import Order


class DeliveryManager(metaclass=MetaSingleton):
    """Класс менеджер доставщиков"""

    def __init__(self):
        self.__areas: list[Area] = [Area() for _ in range(3)]
        self.__matrix_areas_location: list[list[int]] = [[2], [2], [0, 1]]

    def get_orders_status(
            self
    ) -> tuple[list[tuple[str, str]], list[tuple[tuple[str, str], int]]]:
        """Метод возвращает статусы всех заказов"""
        result_orders = [], []
        for area in self.__areas:
            orders = area.get_orders_status()
            result_orders[0].extend(orders[0])
            result_orders[1].extend(orders[1])
        return result_orders

    def accept_order(self, order: Order, road_length: float) -> bool:
        """Метод определяет есть ли свободный доставщик для заказа"""
        self.tick()
        return isinstance(self.__find_deliveryman(order, road_length),
                          DeliveryMan)

    def add_deliveryman(self, deliveryman: DeliveryMan):
        """Метод добавления доставщика"""
        self.__areas[deliveryman.area].add_deliveryman(deliveryman)

    def tick(self):
        for area in self.__areas:
            area.tick()

    def __find_deliveryman(
            self, order: Order, road_length: float
    ) -> Optional[DeliveryMan]:
        """Метод ищет свободных заказчиков для выполнения заказа,
        основываясь на нескольких районах"""
        self.tick()
        deliveryman = self.__areas[order.area].find_deliveryman(road_length,
                                                                order)
        idx: int = 0
        is_another_area: bool = False
        while idx != len(self.__matrix_areas_location[order.area]) and \
                not isinstance(deliveryman, DeliveryMan):
            deliveryman = self.__areas[
                self.__matrix_areas_location[order.area][idx]
            ].find_deliveryman(road_length, order)
            is_another_area = True
            idx += 1
        if isinstance(deliveryman, DeliveryMan):
            deliveryman.current_order = True
            if not is_another_area:
                deliveryman.timer_start(road_length, order.id[0])
            else:
                # random нужен, чтоб симулировать длину дороги из другого
                # района для водителя
                # road_length - meters
                deliveryman.timer_start(
                    road_length + random.randint(0, 200), order.id[0]
                )
        return deliveryman
