import json

from GroceryRetailer import GroceryRetailer
from Product import Product


class GroceryRetailerManager:
    def __init__(self):
        self.__retailers: list[GroceryRetailer] = []

    def __str__(self):
        return f'Список магазинов: {self.__retailers}'

    def add_grocery_retailer(self, retailer: GroceryRetailer):
        self.__retailers.append(retailer)

    def load_json(self, file_path: str):
        with open('resources/GroceryRetailers.json', 'r') as file:
            data = json.load(file)
        for retailer in data:
            self.__retailers.append(
                GroceryRetailer(
                    retailer['name'],
                    retailer['type'],
                    self.load_product_list(retailer['menu']),
                    self.load_product_list(retailer['stop_list'])
                )
            )

    @staticmethod
    def load_product_list(data: list[dict]) -> list[Product]:
        result: list[Product] = []
        for product in data:
            result.append(
                Product(
                    name=product['name'],
                    price=product['price'],
                    weight=product['weight'],
                    composition=product['composition']
                )
            )
        return result
