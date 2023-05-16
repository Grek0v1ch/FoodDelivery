from DelivaryMan import DelivaryMan
from MetaSingleton import MetaSingleton


class DelivaryManager(metaclass=MetaSingleton):
    def __init__(self):
        self.__active_delivers: list[DelivaryMan] = []
        self.__inactive_delivers: list[DelivaryMan] = []
        self.__orders_queue: list[int] = []

    def add_delivaryman(self, deliveryman: DelivaryMan) -> None:
        self.__inactive_delivers.append(deliveryman)

    def tick(self) -> None:
        for deliveryman in self.__active_delivers:
            deliveryman.tick()
            if deliveryman.is_free:
                self.__inactive_delivers.append(deliveryman)

    def process_order(self, order: int, road_length: float) -> None:
        self.tick()
        if len(self.__inactive_delivers) > 0:
            deliveryman = self.__inactive_delivers.pop()
            deliveryman.current_order = order
            # 13 - средняя скорость человека(затычка для расчета времени пути)
            deliveryman.timer_start(road_length)
            self.__active_delivers.append(deliveryman)
        else:
            self.__orders_queue.append(order)

