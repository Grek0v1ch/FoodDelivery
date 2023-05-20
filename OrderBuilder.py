from Order import Order


class OrderBuilder:
    def __int__(self):
        self.__order: Order = Order(1)

    def add_grocery_retailer(self, grocery_retailer_id: int):
        self.__order.grocery_retailer_id = grocery_retailer_id

    def add_area(self, area: int):
        self.__order.area = area

    def add_product(self, product: bool):
        self.__order.current_product = product

    def add_time_cooking(self, time_cooking: int):
        self.__order.time_cooking = time_cooking

    def add_price(self, price: float):
        self.__order.price = price
