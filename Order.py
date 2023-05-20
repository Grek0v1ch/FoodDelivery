from dataclasses import dataclass


@dataclass
class Order:
    area: int
    grocery_retailer_id: int
    current_product: bool  # Product
    time_cooking: int
    price: float
    