''''
Question:
Design an online shopping cart system:
Product class with name, price.
DiscountStrategy (abstract) with method apply_discount().
Subclasses: NoDiscount, PercentageDiscount, FixedDiscount.
Cart class that calculates total price using a chosen discount strategy.
'''

from abc import ABC, abstractmethod

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, amount):
        pass


class NoDiscount(DiscountStrategy):
    def apply_discount(self, amount):
        return amount


class PercentageDiscount(DiscountStrategy):
    def __init__(self, percent):
        self.percent = percent

    def apply_discount(self, amount):
        return amount - (amount * self.percent / 100)


class FixedDiscount(DiscountStrategy):
    def __init__(self, discount):
        self.discount = discount

    def apply_discount(self, amount):
        return max(0, amount - self.discount)


class Cart:
    def __init__(self, discount_strategy):
        self.items = []
        self.discount_strategy = discount_strategy

    def add_item(self, product):
        self.items.append(product)

    def total(self):
        amount = sum(item.price for item in self.items)
        return self.discount_strategy.apply_discount(amount)



cart = Cart(PercentageDiscount(10))  # 10% discount
cart.add_item(Product("Laptop", 50000))
cart.add_item(Product("Mouse", 1000))

print("Total:", cart.total())  # Should apply 10% discount

