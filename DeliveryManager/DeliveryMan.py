from dataclasses import dataclass
from enum import Enum
import time


class TransportType(Enum):
    """integer numbers - speed of transport types in m/s"""
    CAR = 16.67
    SCOOTER = 12.5
    BICYCLE = 6.94
    AFOOT = 3.67


@dataclass
class DeliveryMan:
    area: int
    current_order: bool  # Order
    transport: str
    order_time: float
    time_start: float

    @property
    def is_free(self) -> bool:
        return self.current_order is False

    @property
    def time_left(self):
        return self.order_time - (time.time() - self.time_start)

    def timer_start(self, road_length: float) -> None:
        self.time_start = time.time()
        self.order_time = road_length / TransportType[self.transport].value

    def tick(self) -> None:
        # TODO: стоит добавить что нужно спрашивать у доставщика пришел ли заказ
        if time.time() - self.time_start >= self.order_time:
            self.current_order = False
