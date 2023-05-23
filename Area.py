from typing import Optional, Union

from DelivaryMan import DelivaryMan


class Area:
    def __init__(self):
        self.delivers = {}
        sample = {'active': Optional[list[DelivaryMan]],
                  'inactive': Optional[list[DelivaryMan]]}
        self.delivers['AFOOT'] = sample
        self.delivers['CAR'] = sample
        self.delivers['BICYCLE'] = sample
        self.delivers['SCOOTER'] = sample

    def tick(self):
        for key in self.delivers.keys():
            for deliveryman in self.delivers[key]['active']:
                deliveryman.tick()
                if deliveryman.is_free:
                    self.delivers[key]['inactive'].append(deliveryman)

    def add_delivaryman(self, delivaryman: DelivaryMan):
        self.delivers[delivaryman.transport]['inactive'].append(delivaryman)

    def find_delivaryman(self, road_length: float) -> Union[DelivaryMan, bool]:
        idx: int = 0

        if road_length < 850:
            idx = 0
        elif road_length < 1700:
            idx = 1
        elif road_length < 3000:
            idx = 2
        else:
            idx = 3

        for key in self.delivers.keys():
            if idx != 0:
                idx -= 1
                continue
            if len(self.delivers[key]['inactive']):
                deliveryman = self.delivers[key]['inactive'].pop()
                self.delivers[key]['active'].append(deliveryman)
                return deliveryman
        return False




