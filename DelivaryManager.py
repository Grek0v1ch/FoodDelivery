from DelivaryMan import DelivaryMan, OrderStatus
from MetaSingleton import MetaSingleton


class DelivaryManager(metaclass=MetaSingleton):
    def __init__(self):
        self.__active_delivers: list[DelivaryMan] = []
        self.__inactive_delivers: list[DelivaryMan] = []
        self.__orders_queue: list[Order] = []

    def add_delivaryman(self, deliveryman: DelivaryMan) -> None:
        self.__inactive_delivers.append(deliveryman)

    def tick(self) -> None:
        for deliveryman in self.__active_delivers:
            deliveryman.tick()
            if deliveryman.delivary_status == OrderStatus.FREE:
                deliveryman.current_order = None
            if deliveryman.is_free:
                if len(self.__orders_queue) > 0:
                    deliveryman.current_task = self.__orders_queue.pop()
                else:
                    self.__inactive_delivers.append(deliveryman)

    def process_order(self, order: Order) -> None:
        if len(self.__inactive_delivers) > 0:
            deliverman = self.__inactive_delivers.pop()
            deliverman.current_order = order
            self.__active_delivers.append(deliverman)
        else:
            self.__orders_queue.append(order)

