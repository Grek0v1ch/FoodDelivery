from typing import Union, Dict
from DeliveryMan import DeliveryMan


def define_initial_transport_idx(distance: float) -> int:
    """ Transport's idx:
    AFOOT - 0
    BICYCLE - 1
    SCOOTER - 2
    CAR - 3
    """
    if distance < 850:
        idx = 0
    elif distance < 1700:
        idx = 1
    elif distance < 3000:
        idx = 2
    else:
        idx = 3
    return idx


class Area:
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

    def tick(self):
        for key in self.area_delivery.keys():
            for deliveryman in self.area_delivery[key]['active']:
                deliveryman.tick()
                if deliveryman.is_free:
                    self.area_delivery[key]['inactive'].append(deliveryman)

    def add_deliveryman(self, deliveryman: DeliveryMan):
        self.area_delivery[deliveryman.transport]['inactive'].append(deliveryman)

    def find_delivaryman(self, road_length: float) -> Union[DeliveryMan, None]:
        """find deliveryman based on path length"""
        idx: int = define_initial_transport_idx(road_length)

        for key in list(self.area_delivery.keys())[idx:]:
            if len(self.area_delivery[key]['inactive']):
                deliveryman = self.area_delivery[key]['inactive'].pop()
                self.area_delivery[key]['active'].append(deliveryman)
                return deliveryman
        return None
