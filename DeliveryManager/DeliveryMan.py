from dataclasses import dataclass
from enum import Enum
import time

import telegram_bot


class TransportType(Enum):
    """Скорость всех видов транспорта доставщиков"""
    CAR = 16.67
    SCOOTER = 12.5
    BICYCLE = 6.94
    AFOOT = 3.67


@dataclass
class DeliveryMan:
    """Класс доставщика"""
    id: tuple[str]
    area: int
    current_order: bool
    transport: str
    order_time: float
    order_id: str
    time_start: float

    @property
    def is_free(self) -> bool:
        """Метод определяет свободен ли доставщик"""
        return self.current_order is False

    @property
    def time_left(self) -> float:
        """Метод определяет оставшееся время до выполнения заказа"""
        if self.order_time - (time.time() - self.time_start) < 0:
            return 0
        else:
            return self.order_time - (time.time() - self.time_start)

    def timer_start(self, road_length: float, order_id: str):
        """Метод отсчитывает начало выполнения заказа"""
        self.order_id = order_id
        self.time_start = time.time()
        self.order_time = road_length / TransportType[self.transport].value

    def tick(self) -> None:
        """Метод определяет доставлен заказ или нет"""
        if time.time() - self.time_start >= self.order_time:
            telegram_bot.ask_deliveryman_to_skip(int(self.id[0]))
            if telegram_bot.CLOSE_ANS[int(self.id[0])]:
                self.current_order = False
            else:
                self.order_time += 30
