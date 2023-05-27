from dataclasses import dataclass
from enum import Enum
import time


class TransportType(Enum):
    """integer numbers - speed of transport types"""
    CAR = 60
    SCOOTER = 45
    BICYCLE = 25
    AFOOT = 13


def translate_hours_to_seconds(hours: float) -> float:
    return hours * 3600


@dataclass
class DelivaryMan:
    area: int
    current_order: bool  # Order
    transport: str
    order_time: float
    time_start: float

    @property
    def is_free(self) -> bool:
        return self.current_order is False

    def timer_start(self, road_length: float) -> None:
        self.time_start = time.time()
        self.order_time = translate_hours_to_seconds(road_length / TransportType[self.transport].value)
        print(self.transport, self.area)

    def tick(self) -> None:
        # TODO: стоит добавить что нужно спрашивать у доставщика пришел ли заказ
        if time.time() - self.time_start >= self.order_time and self.time_start != -1:
            self.current_order = False
            self.time_start = -1
            print(self.area, self.transport, time.time() - self.time_start)
