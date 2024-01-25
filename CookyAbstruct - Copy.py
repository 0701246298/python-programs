from abc import ABC, abstractmethod

class Item(ABC):
    @abstractmethod
    def get_item_name(self) -> str:
        pass

    @abstractmethod
    def set_price(self, price: int):
        pass

    @abstractmethod
    def get_price(self) -> int:
        pass

    @abstractmethod
    def get_department(self) -> str:
        pass

class Cookie(Item):
    def __init__(self, item_name: str, price: int, department: str):
        self.item_name = item_name
        self.price = price
        self.department = department

    def get_item_name(self) -> str:
        return self.item_name

    def set_price(self, price: int):
        self.price = price

    def get_price(self) -> int:
        return self.price

    def get_department(self) -> str:
        return self.department

# Create a Cookie object
my_cookie = Cookie("Chocolate Chip Cookie", 2, "Bakery")

# Accessing information about the cookie
print(f"Item Name: {my_cookie.get_item_name()}")
print(f"Price: ${my_cookie.get_price()}")
print(f"Department: {my_cookie.get_department()}")
