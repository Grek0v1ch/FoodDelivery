from GroceryRetailerManager import GroceryRetailerManager


def main():
    manager = GroceryRetailerManager()
    manager.load_json('resources/GroceryRetailers.json')
    manager.make_order()


if __name__ == "__main__":
    main()
