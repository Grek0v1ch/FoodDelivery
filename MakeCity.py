import json

from DeliveryManager.Area import Area


def check_input_areas(num_area: int, num_areas: int) -> list:
    while True:
        try:
            input_areas = [int(area) for area in input(
                f'Для района {num_area} '
                f'укажите список районов, '
                f'с которыми он может '
                f'взаимодействовать: ').split()]
            if num_area in input_areas:
                print('В списке районов не должен быть указан тот район, '
                      'для которого устанавливается взаимодействие. '
                      'Повторите ввод.')
            elif any(map(lambda x: x > num_areas - 1, input_areas)):
                print('Номер района не должен превосходить '
                      '(общее кол-во районов - 1).'
                      'Повторите ввод.')
            elif any(map(lambda x: input_areas.count(x) > 1, input_areas)):
                print('Несколько раз введен один и тот же номер района. '
                      'Повторите ввод.')
            else:
                return input_areas
        except ValueError:
            print('Введенное значение не является целым числом.'
                  ' Повторите ввод')
            pass


class MakeCity:
    def __init__(self):
        self.num_areas = int(input("Введите количество районов: "))
        self.areas = [Area() for _ in range(self.num_areas)]
        self.matrix_areas_location = [[] for _ in range(self.num_areas)]
        for num_area in range(self.num_areas):
            self.matrix_areas_location[num_area] = \
                check_input_areas(num_area, self.num_areas)
        with open('city.json', 'w') as out_file:
            city_data = {
                'num_areas': self.num_areas,
                'matrix_areas_location': self.matrix_areas_location
            }
            out_json = json.dumps(city_data, indent=4)
            out_file.write(out_json)
