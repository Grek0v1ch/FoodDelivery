from dataclasses import dataclass
from enum import Enum


class TransportType(Enum):
    CAR = 1
    SCOOTER = 2
    BICYCLE = 3
    AFOOT = 4


@dataclass
class DelivaryMan:
    curr_order: Order
    transport: TransportType
    time: int
