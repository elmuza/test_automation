
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, name, price, quantity=1):
        if price < 0:
            raise ValueError("Цена не может быть отрицательной")

        if quantity <= 0:
            raise ValueError("Количество должно быть больше нуля")

        item = {
            "name": name,
            "price": price,
            "quantity": quantity
        }

        self.items.append(item)

    def get_total(self):
        total = 0

        for item in self.items:
            total += item["price"] * item["quantity"]

        return total

    def get_item_count(self):
        return sum(item["quantity"] for item in self.items)

    def remove_item(self, name):
        for item in self.items:
            if item["name"] == name:
                self.items.remove(item)
                return True

        return False

    def clear(self):
        self.items.clear()

