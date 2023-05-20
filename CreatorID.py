import uuid


class CreatorID:
    @staticmethod
    def generate_order_id() -> tuple[str]:
        return 'order' + str(uuid.uuid4()),

    @staticmethod
    def generate_grocery_retailer_id() -> tuple[str]:
        return 'grocery_retailer' + str(uuid.uuid4()),

    @staticmethod
    def generate_deliveryman_id() -> tuple[str]:
        return 'deliveryman' + str(uuid.uuid4()),
