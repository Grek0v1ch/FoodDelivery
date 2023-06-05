import random
from typing import Optional

from DeliveryManager.DeliveryMan import DeliveryMan
from DeliveryManager.Area import Area
from MetaSingleton import MetaSingleton
from Order.Order import Order

CAR_DISTANCE = 3000


class DeliveryManager(metaclass=MetaSingleton):
    def __init__(self):
        # TODO: сделать отдельный класс город для создания районов
        self.__areas: list[Area] = [Area() for _ in range(3)]
        # TODO: обсудить программу заполнения матрицы районов
        self.__matrix_areas_location: list[list[int]] = [[2], [2], [0, 1]]

    def get_orders_status(self) -> \
           Optional[tuple[list[str], list[tuple[str, int]]]]:
        result_orders: tuple[list[str], list[tuple[str, int]]] = [], []
        for area in self.__areas:
            orders: tuple[list[str], list[tuple[str, int]]] = \
                area.get_orders_status()
            result_orders[0].extend(orders[0])
            result_orders[1].extend(orders[1])
        return result_orders

    def accept_order(self, order: Order, road_length: float):
        return self.__find_deliveryman(order, road_length) is DeliveryMan

    def add_deliveryman(self, deliveryman: DeliveryMan) -> None:
        self.__areas[deliveryman.area].add_deliveryman(deliveryman)

    def tick(self) -> None:
        for area in self.__areas:
            area.tick()

    def __find_deliveryman(self, order: Order, road_length: float) -> \
            Optional[DeliveryMan]:
        """if we can't find deliveryman in area we start find him in neighboring area"""
        self.tick()
        deliveryman = self.__areas[order.area].find_delivaryman(road_length,
                                                                order)
        idx: int = 0
        is_another_area: bool = False
        while idx != len(self.__matrix_areas_location[order.area]) and not \
                isinstance(deliveryman, DeliveryMan):
            deliveryman = self.__areas[self.__matrix_areas_location[order.area][
               idx]].find_delivaryman(road_length, order)
            is_another_area = True
            idx += 1
        if isinstance(deliveryman, DeliveryMan):
            deliveryman.current_order = True
            if not is_another_area:
                deliveryman.timer_start(road_length)
            else:
                # random нужен, чтоб симулировать длину дороги из другого
                # района для водителя
                # road_length - meters
                deliveryman.timer_start(road_length + random.randint(0, 2000))
        return deliveryman
