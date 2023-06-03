from typing import Union
from Area import Area
from DeliveryMan import DeliveryMan
from MetaSingleton import MetaSingleton
from Order import Order


class DeliveryManager(metaclass=MetaSingleton):
    def __init__(self):
        # TODO: сделать отдельный класс город для создания районов
        self.__areas: list[Area] = [Area() for _ in range(3)]
        # TODO: обсудить программу заполнения матрицы районов
        self.__matrix_areas_location: list[list[int]] = [[2], [2], [0, 1]]

    def add_deliveryman(self, deliveryman: DeliveryMan) -> None:
        self.__areas[deliveryman.area].add_deliveryman(deliveryman)

    def tick(self) -> None:
        for area in self.__areas:
            area.tick()

    def find_deliveryman(self, order: Order, road_length: float) -> \
            Union[DeliveryMan, None]:
        """if we can't find deliveryman in area we start find him in neighboring area"""
        self.tick()
        deliveryman = self.__areas[order.area].find_delivaryman(road_length)
        idx: int = 0
        while idx != len(self.__matrix_areas_location[order.area]) and not \
                isinstance(deliveryman, DeliveryMan):
            deliveryman = self.__areas[self.__matrix_areas_location[order.area][
                idx]].find_delivaryman(3000)
            idx += 1
        if isinstance(deliveryman, DeliveryMan):
            deliveryman.current_order = True
            deliveryman.timer_start(road_length)
        return deliveryman
