from inventory.inventory_implementation import InventoryImplementation
from abc import ABC
from command.command import Command

class ChangePriceCommand(Command, ABC):
    """Implements the command class for adding a book."""
    def __init__(self, inventory_object, new_price):
        self.inventory_object = inventory_object
        self.new_price = new_price

    def execute(self, book_identity):
        self.inventory_object.change_price_of_book(book_identity, self.new_price)

    def serialize(self, book_identity):
        """
        Serialize the command executed into a text format with command identifier to be stored into the command file.
        :param book_payload:
        :return:
        """
        found_book = self.inventory_object.get_book(book_identity)
        return "{},{},{},{},{}".format(found_book['name'], found_book['price'], found_book['id'], found_book['quantity'], "CHANGE_PRICE")
