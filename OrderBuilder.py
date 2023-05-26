from CreatorID import CreatorID
from Order import Order
from Product import Product


class OrderBuilder:
    def __init__(self):
        self.__order: Order = Order(CreatorID.generate_order_id())

    def add_grocery_retailer(self, grocery_retailer_id: tuple[str]):
        self.__order.grocery_retailer_id = grocery_retailer_id

    def add_area(self, area: int):
        self.__order.area = area

    def add_product(self, product: Product):
        if self.__order.products is None:
            self.__order.products = []
        self.__order.products.append(product)

    def add_time_cooking(self, time_cooking: int):
        self.__order.time_cooking = time_cooking

    def add_price(self, price: float):
        if self.__order.price is None:
            self.__order.price = 0
        self.__order.price += price

    @property
    def order(self) -> Order:
        return self.__order
