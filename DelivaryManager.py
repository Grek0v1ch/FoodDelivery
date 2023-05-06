from DelivaryMan import DelivaryMan
from MetaSingleton import MetaSingleton


class DelivaryManager(metaclass=MetaSingleton):
    def __init__(self):
        self.__delivers: list[DelivaryMan] = []

    def add_delivaryman(self, deliveryman: DelivaryMan):
        self.__delivers.append(deliveryman)

    def process_order(self):
        pass

