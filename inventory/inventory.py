"""
author: Melrick
"""
from abc import ABC, abstractmethod

class Inventory(ABC):
    """Abstract class for defining the methods in an Inventory class for storing the objects."""
    @abstractmethod
    def add_book(self, book_payload):
        pass

    @abstractmethod
    def find_book(self, book_identity):
        pass

    @abstractmethod
    def display_book_details(self, index):
        pass

    @abstractmethod
    def sell_book(self, book_identity):
        pass

    @abstractmethod
    def add_book_copies(self, book_identity, book_quantity):
        pass

    @abstractmethod
    def change_price_of_book(self, book_identity, new_price):
        pass