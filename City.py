import json
from DeliveryManager.Area import Area


class City:
    def __init__(self):
        with open('city.json', 'r') as inp_file:
            city_data = json.load(inp_file)
        self.num_areas = city_data['num_areas']
        self.areas = [Area() for _ in range(self.num_areas)]
        self.matrix_areas_location = city_data['matrix_areas_location']
