from inventory.inventory_implementation import InventoryImplementation
from abc import ABC
from command.command import Command

class AddBookCommand(Command, ABC):
    """Implements the command class for adding a book."""
    def __init__(self, inventory_object):
        self.inventory_object = inventory_object

    def execute(self, book_payload):
        self.inventory_object.add_book(book_payload)

    def serialize(self, book_payload):
        """
        Serialize the command executed into a text format with command identifier to be stored into the command file.
        :param book_payload:
        :return:
        """
        return "{},{},{},{},{}".format(book_payload.name, book_payload.price, book_payload.id, book_payload.quantity, "ADD_BOOK")
