from dataclasses import dataclass
from enum import Enum


class TransportType(Enum):
    CAR = 1
    SCOOTER = 2
    BICYCLE = 3
    AFOOT = 4


class OrderStatus(Enum):
    FREE = 0
    EXECUTING = 1


@dataclass
class DelivaryMan:
    current_order: Order
    transport: TransportType
    time: int

    @property
    def is_free(self) -> bool:
        return self.current_order is None

    @property
    def delivary_status(self):
        if self.current_order is None:
            return OrderStatus.FREE
        else:
            return OrderStatus.EXECUTING
