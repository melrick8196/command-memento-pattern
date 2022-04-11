import unittest
from inventory.inventory_decorator import InventoryDecorator
from book import Book

class AddBookTest(unittest.TestCase):
    """Unit test class for performing the addition of book to log file which implements command pattern, decorator pattern and memento pattern"""
    # def __init__(self, inventory_data):
    #     self.inventory_data = inventory_data

    def add_book_test(self):
        b1 = Book('Harry', 13, 10)
        bookstore = InventoryDecorator()
        bookstore.add_book_command(b1)
        bookstore.save_memento()
        self.assertEqual(b1.name, bookstore.inventory_data['books'][0]['name'])
