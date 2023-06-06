from dataclasses import dataclass
from typing import Optional


@dataclass
class Product:
    """
    Класс для представления продукта.

    Атрибуты:
    name : str
        название продукта
    price : int
        стоимость продукта
    weight : int
        вес продукта
    composition : list
        составляющие продукта
    time_cooking : int
        время приготовления продукта
    """
    name: Optional[str] = None
    price: Optional[float] = None
    weight: Optional[int] = None
    composition: Optional[str] = None
    time_cooking: Optional[int] = None

    def __str__(self):
        """
        Возвращает всё информацию о продукте (название, стоимость, вес, состав
        и время приготовления).
        """
        return f'Имя: {self.name}, Стоимость: {self.price}, ' \
               f'Вес: {self.weight}, Состав: {self.composition}, ' \
               f'Время приготовления: {self.time_cooking}'
