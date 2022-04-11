import unittest
from inventory.inventory_decorator import InventoryDecorator
from book import Book

class SellBookTest(unittest.TestCase):
    """Unit test class for performing the selling of book to log file which implements command pattern, decorator pattern and memento pattern"""
    def __init__(self, inventory_data):
        self.inventory_data = inventory_data

    def sell_book_test(self):
        # bookstore = InventoryDecorator()
        # bookstore.get_state()
        print(bookstore.inventory_data['books'])
        self.assertEqual('Harry', bookstore.inventory_data['books'][0]['name'])