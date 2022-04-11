"""
Filename: inventory_implementation.py
author: Melrick
"""

from dataclasses import dataclass
from book import Book
import json
from inventory.inventory import Inventory


class InventoryImplementation(Inventory):
    """Class which implements the Inventory interface"""
    def __init__(self):
        """
        Dictionary object inventory_data will store all the object files.
        """
        self.inventory_data = {}
        self.inventory_data["books"] = []
        self.count = 0

    def add_book(self, book_payload):
        """
        Check if book already exists by name and add, if it exists then increment the book by the quantity specified.
        :param book_payload:
        :return:
        """
        index = self.find_book(book_payload.name)
        if index:
            print("book already exists! increasing the count")
            old_value = int(self.inventory_data["books"][index]['quantity'])
            new_vale = old_value + int(book_payload.quantity)
            self.inventory_data["books"][index]['quantity'] = str(new_vale)
        else:
            new_id = len(self.inventory_data["books"])
            new_id += 1
            book_payload.id = new_id
            self.inventory_data["books"].append(dict(book_payload))

    def find_book(self, book_identity):
        """
        Returns the index of the found book.
        :param book_identity:
        :return:
        """
        total = len(self.inventory_data["books"])
        if book_identity.isdigit():
            for i in range(total):
                if int(book_identity) == self.inventory_data["books"][i]['id']:
                    return i
        else:
            for i in range(total):
                if book_identity in self.inventory_data["books"][i]['name']:
                    return i
        return False

    # def find_book_by_id(self, book_id):
    #     total = len(self.inventory_data["books"])
    #     for i in range(total):
    #         if book_id == self.inventory_data["books"][i]['id']:
    #             return i
    #     return "Not found!"

    def display_book_details(self, index):
        return self.inventory_data["books"][index]

    def sell_book(self, book_identity):
        """
        Function to sell the book details
        :param book_identity:
        :return:
        """
        index = self.find_book(book_identity)
        if self.inventory_data["books"][index]['quantity'] == 0:
            return "Book is not available to sell"
        else:
            self.inventory_data["books"][index]['quantity'] -= 1

    def add_book_copies(self, book_identity, book_quantity):
        index = self.find_book(book_identity)
        self.inventory_data["books"][index]['quantity'] += book_quantity

    def change_price_of_book(self, book_identity, new_price):
        index = self.find_book(book_identity)
        print(index)
        self.inventory_data["books"][index]['price'] = new_price

    def get_book(self, book_identity):
        """
        Returns the book dict from the given identity
        :param book_identity:
        :return:
        """
        index = self.find_book(book_identity)
        return self.inventory_data["books"][index]
