from dataclasses import dataclass
from enum import Enum
import time


class TransportType(Enum):
    CAR = 1
    SCOOTER = 2
    BICYCLE = 3
    AFOOT = 4


def translate_hours_to_seconds(hours: float) -> float:
    return hours * 3600


@dataclass
class DelivaryMan:
    area: int
    current_order: bool  # Order
    transport: TransportType
    order_time: float
    time_start: float

    @property
    def is_free(self) -> bool:
        return self.current_order is False

    def timer_start(self, road_length: float):
        self.time_start = time.time()
        # 60, 45, 20, 13 - средние скорости транспортных средств
        if self.transport == TransportType.CAR.value:
            self.order_time = road_length / 60
        elif self.transport == TransportType.SCOOTER.value:
            self.order_time = road_length / 45
        elif self.transport == TransportType.BICYCLE.value:
            self.order_time = road_length / 20
        elif self.transport == TransportType.AFOOT.value:
            self.order_time = road_length / 13
        # перевод в секунды
        self.order_time = translate_hours_to_seconds(self.order_time)

    def tick(self) -> None:
        # стоит добавить что нужно спрашивать у доставщика пришел ли заказ
        if time.time() - self.time_start >= self.order_time:
            self.current_order = False
