from CreatorID import CreatorID
from GroceryRetailer.GroceryRetailer import GroceryRetailer
from Order.Order import Order
from Order.Product import Product


class OrderBuilder:
    def __init__(self):
        self.__order: Order = Order(CreatorID.generate_order_id())

    def add_grocery_retailer(self, grocery_retailer: GroceryRetailer):
        self.__order.grocery_retailer_id = grocery_retailer.id
        self.__order.area = grocery_retailer.area
        self.__order.price = 0
        self.__order.weight = 0
        self.__order.time_cooking = 0
        self.__order.products = []

    def add_product(self, product: Product):
        if self.__order.grocery_retailer_id is None:
            return
        self.__order.products.append(product)
        self.__order.price += product.price
        self.__order.weight += product.weight
        self.__order.time_cooking += product.time_cooking

    @property
    def order(self) -> Order:
        return self.__order
