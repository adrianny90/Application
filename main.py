class Item:
    def __init__(self, name, price, quantity=4):
        # Validation for inputs
        assert price >= 0, f"Price {price} is not bigger than 0"
        assert quantity >= 0
        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    @staticmethod
    def calculate_price(x, y):
        return x * y


item1 = Item("phone", 100)
item2 = Item("Laptop", 1200)

item2.has_numpad = False
print(item1.name, item2.has_numpad)
print(item1.calculate_price(item2.price, item2.quantity))
print(Item.__dict__)
print(item2.__dict__)
