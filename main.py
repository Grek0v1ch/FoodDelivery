from GroceryRetailer.GroceryRetailerManager import GroceryRetailerManager


def main():
    manager = GroceryRetailerManager()
    manager.load_json('resources/GroceryRetailers.json')
    order = manager.make_order()
    print(order)


if __name__ == "__main__":
    main()
