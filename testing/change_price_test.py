import unittest
from inventory.inventory_decorator import InventoryDecorator
from book import Book

class ChangePriceTest(unittest.TestCase):
    """Unit test class for performing the change of price of book to log file which implements command pattern, decorator pattern and memento pattern"""
    def __init__(self, inventory_data):
        self.inventory_data = inventory_data

    def change_price_test(self):
        bookstore = InventoryDecorator()
        bookstore.get_state()
        bookstore.change_price_of_book_command('Harry', 200)
        self.assertEqual(200, bookstore.inventory_data['books'][0]['price'])