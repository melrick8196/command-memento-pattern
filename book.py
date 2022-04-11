"""
Filename: book.py
author: Melrick
"""

from dataclasses import dataclass
from decimal import Decimal

@dataclass
class Book:
    """Class for holding book details"""
    name: str = None
    price: Decimal = None
    quantity: int = None
    id: int = None

    def __init__(self, name, price, quantity, id=None):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __dict__(self):
        """
        Overiding the dict() to store in a json object
        :return:
        """
        return {"name": self.name, "price": self.price, "id": self.id, "quantity": self.quantity}

    def __iter__(self):
        book_obj = {"name": self.name, "price": self.price, "id": self.id, "quantity": self.quantity}
        for key in book_obj.items():
            yield key
