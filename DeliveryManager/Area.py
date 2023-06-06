from typing import Dict, Optional
from DeliveryManager.DeliveryMan import DeliveryMan
from Order.Order import Order

DISTANCES: tuple = (850, 1700, 3000)


def define_initial_transport_idx(distance: float, order: Order) -> int:
    """
    Transport's idx:
    AFOOT - 0
    BICYCLE - 1
    SCOOTER - 2
    CAR - 3
    """
    transport_idx: int = 0
    if order.weight < 15000:
        while distance > DISTANCES[transport_idx] and transport_idx < 3:
            transport_idx += 1
    else:
        transport_idx = 3
    return transport_idx


class Area(object):
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
        self.__deliveryman_status: Dict[str, tuple[Order, DeliveryMan]] = {}

    def tick(self):
        for key in self.area_delivery.keys():
            for deliveryman in self.area_delivery[key]['active']:
                deliveryman.tick()
                if deliveryman.is_free:
                    self.area_delivery[key]['inactive'].append(deliveryman)

    def get_orders_status(self) -> \
            Optional[tuple[list[tuple[str, str]], list[tuple[tuple[str, str], int]]]]:
        ready_orders_id: list[str] = []
        ready_orders: list[tuple[str, str]] = []
        active_orders: list[tuple[tuple[str, str], int]] = []
        for order_id in self.__deliveryman_status.keys():
            if self.__deliveryman_status[order_id][1].time_left <= 0:
                ready_orders.append((order_id, self.__deliveryman_status[order_id][1].id[0]))
                ready_orders_id.append(order_id)
            else:
                active_orders.append(
                    ((order_id, self.__deliveryman_status[order_id][1].id[0]),
                     int(self.__deliveryman_status[order_id][1].time_left)))
        for order_id in ready_orders_id:
            self.__deliveryman_status.pop(order_id)
        return ready_orders, active_orders

    def add_deliveryman(self, deliveryman: DeliveryMan):
        self.area_delivery[deliveryman.transport]['inactive'].append(
            deliveryman)

    def find_delivaryman(self, road_length: float, order: Order) -> Optional[
                                                                    DeliveryMan]:
        """find deliveryman based on path length"""
        idx: int = define_initial_transport_idx(road_length, order)

        for key in list(self.area_delivery.keys())[idx:]:
            if len(self.area_delivery[key]['inactive']):
                deliveryman = self.area_delivery[key]['inactive'].pop()
                self.area_delivery[key]['active'].append(deliveryman)
                self.__deliveryman_status[order.id[0]] = (order, deliveryman)
                return deliveryman
        return None
