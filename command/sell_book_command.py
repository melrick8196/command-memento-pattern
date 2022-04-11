from inventory.inventory_implementation import InventoryImplementation
from abc import ABC
from command.command import Command

class SellBookCommand(Command, ABC):
    """Implements the command class for selling a book."""
    def __init__(self, inventory_object):
        self.inventory_object = inventory_object

    def execute(self, book_identity):
        self.inventory_object.sell_book(book_identity)

    def serialize(self, book_identity):
        """
        Serialize the command executed into a text format with command identifier to be stored into the command file.
        :param book_payload:
        :return:
        """
        found_book = self.inventory_object.get_book(book_identity)
        print(found_book)
        return "{},{},{},{},{}".format(found_book['name'], found_book['price'], found_book['id'], found_book['quantity'], "SELL_BOOK")