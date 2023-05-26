from typing import Union, Dict

from DelivaryMan import DelivaryMan


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
        self.delivers: Dict[str, Dict[str, list[DelivaryMan]]] = {'AFOOT': {'active': [],
                                                                            'inactive': []},
                                                                  'BICYCLE': {'active': [],
                                                                              'inactive': []},
                                                                  'SCOOTER': {'active': [],
                                                                              'inactive': []},
                                                                  'CAR': {'active': [],
                                                                          'inactive': []}
                                                                  }

    def tick(self):
        for key in self.delivers.keys():
            for deliveryman in self.delivers[key]['active']:
                deliveryman.tick()
                if deliveryman.is_free:
                    self.delivers[key]['inactive'].append(deliveryman)

    def add_delivaryman(self, delivaryman: DelivaryMan):
        self.delivers[delivaryman.transport]['inactive'].append(delivaryman)

    def find_delivaryman(self, road_length: float) -> Union[DelivaryMan, bool]:
        """find deliveryman based on path length"""
        idx: int = define_initial_transport_idx(road_length)

        for key in list(self.delivers.keys())[idx:]:
            if len(self.delivers[key]['inactive']):
                deliveryman = self.delivers[key]['inactive'].pop()
                self.delivers[key]['active'].append(deliveryman)
                return deliveryman
        return False
