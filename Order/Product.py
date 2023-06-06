from dataclasses import dataclass
from typing import Optional


@dataclass
class Product:
    name: Optional[str] = None
    price: Optional[float] = None
    weight: Optional[int] = None
    composition: Optional[str] = None
    time_cooking: Optional[int] = None

    def __str__(self):
        return f'Имя: {self.name}, Стоимость: {self.price}, ' \
               f'Вес: {self.weight}, Состав: {self.composition}, ' \
               f'Время приготовления: {self.time_cooking}'
