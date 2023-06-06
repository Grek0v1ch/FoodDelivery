from typing import Dict, Optional

import telegram_bot
from DeliveryManager.DeliveryMan import DeliveryMan
from Order.Order import Order
# from telegram_bot import ACCEPT_ANS, ask_deliveryman
import time
DISTANCES: tuple = (850, 1700, 3000)


def define_initial_transport_idx(distance: float, order: Order) -> int:
    """
    Индексы транспорта:
    AFOOT - 0
    BICYCLE - 1
    SCOOTER - 2
    CAR - 3
    Метод возвращает необходимый для заказа транспорт
    """
    transport_idx: int = 0
    if order.weight < 15000:
        while distance > DISTANCES[transport_idx] and transport_idx < 3:
            transport_idx += 1
    else:
        transport_idx = 3
    return transport_idx


class Area:
    """Класс района в городе"""
    def __init__(self):
        self.area_delivery: Dict[str, Dict[str, list[DeliveryMan]]] = \
            {'AFOOT': {'active': [],
                       'inactive': []},
             'BICYCLE': {'active': [],
                         'inactive': []},
             'SCOOTER': {'active': [],
                         'inactive': []},
             'CAR': {'active': [],
                     'inactive': []}
             }
        # словарь для хранения доставщика и заказа по id заказа
        self.__deliveryman_status: Dict[str, tuple[Order, DeliveryMan]] = {}
        self.ready_orders: list[tuple[str, str]] = []

    def tick(self):
        """Метод меняет состояние доставщиков"""
        for key in self.area_delivery.keys():
            save_deliveryman: list[DeliveryMan] = []
            for deliveryman in self.area_delivery[key]['active']:
                deliveryman.tick()
                if deliveryman.is_free:
                    self.area_delivery[key]['inactive'].append(deliveryman)
                    self.ready_orders.append(
                        (deliveryman.order_id, deliveryman.id[0])
                    )
                    self.__deliveryman_status.pop(deliveryman.order_id)
                else:
                    save_deliveryman.append(deliveryman)
            self.area_delivery[key]['active'].clear()
            self.area_delivery[key]['active'] = save_deliveryman

    def get_orders_status(
            self
    ) -> tuple[list[tuple[str, str]], list[tuple[tuple[str, str], int]]]:
        """Метод возвращает состояние по всем доставщикам в районе"""
        ready_orders: list[tuple[str, str]] = self.ready_orders.copy()
        self.ready_orders.clear()
        active_orders: list[tuple[tuple[str, str], int]] = []
        for order_id in self.__deliveryman_status.keys():
            active_orders.append((
                (order_id, self.__deliveryman_status[order_id][1].id[0]),
                int(self.__deliveryman_status[order_id][1].time_left)
            ))
        return ready_orders, active_orders

    def add_deliveryman(self, deliveryman: DeliveryMan):
        """Метод добавляет доставщика"""
        self.area_delivery[deliveryman.transport]['inactive'].append(
            deliveryman
        )

    def find_deliveryman(
            self, road_length: float, order: Order
    ) -> Optional[DeliveryMan]:
        """Метод поиска доставщика, основываясь на длине дороги и весе"""
        idx: int = define_initial_transport_idx(road_length, order)
        if order.id not in telegram_bot.ORDER_QUEUE:
            telegram_bot.ORDER_QUEUE.append(order.id)
        if order.id not in telegram_bot.UNWANTED_ORDER.keys():
            telegram_bot.UNWANTED_ORDER[order.id] = []
        for key in list(self.area_delivery.keys())[idx:]:
            for idx, deliveryman in enumerate(self.area_delivery[key]
                                              ['inactive']):
                telegram_bot.NOW_ASK[0] = int(deliveryman.id[0])
                telegram_bot.ask_deliveryman(int(deliveryman.id[0]),
                                             road_length)
                time.sleep(10)
                if telegram_bot.ACCEPT_ANS[int(deliveryman.id[0])]:
                    deliveryman = self.area_delivery[key]['inactive'][idx]
                    del self.area_delivery[key]['inactive'][idx]
                    self.area_delivery[key]['active'].append(deliveryman)
                    self.__deliveryman_status[order.id[0]] = (order, deliveryman)
                    telegram_bot.CLOSE_ANS[int(deliveryman.id[0])] = False
                    telegram_bot.UNWANTED_ORDER.pop(order.id)
                    telegram_bot.ORDER_QUEUE.pop(0)
                    return deliveryman

        return None
