"""
Filename: inventory_implementation.py
author: Melrick
"""

import json
from inventory.inventory_implementation import InventoryImplementation
from command.add_book_command import AddBookCommand
from command.sell_book_command import SellBookCommand
from command.change_price_command import ChangePriceCommand
from memento.inventory_memento import InventoryMemento
from book import Book
from os.path import exists

class InventoryDecorator(InventoryImplementation):
    """Decorator class which decorates and implements the Inventory class. Uses command pattern to add details into the Inventory object."""
    def __init__(self):
        self.MAX_COMMANDS = 10
        self.command_counter = 0
        InventoryImplementation.__init__(self)

    def add_book_command(self, book_payload):
        """
        Uses the command pattern to add the book into the inventory
        :param book_payload:
        :return:
        """
        command = AddBookCommand(self)
        command.execute(book_payload)
        self.write_cmd_to_file(command.serialize(book_payload))

    def sell_book_command(self, book_identity):
        """
        Uses the command pattern to sell the book from the inventory
        :param book_identity:
        :return:
        """
        command = SellBookCommand(self)
        command.execute(book_identity)
        self.write_cmd_to_file(command.serialize(book_identity))

    def change_price_of_book_command(self, book_identity, new_price):
        """
        Uses the command pattern to change the price of the book from the inventory
        :param book_identity:
        :param new_price:
        :return:
        """
        command = ChangePriceCommand(self, new_price)
        command.execute(book_identity)
        self.write_cmd_to_file(command.serialize(book_identity))

    def write_cmd_to_file(self, command_data):
        """
        Serilizes the state change command and stores it in the command.log file.
        :param single_command:
        :return:
        """
        with open('command.log', 'a+') as command_file:
            if self.command_counter < self.MAX_COMMANDS:
                command_file.write(command_data+"\n")
                self.command_counter += 1
                command_file.close()
            else:
                self.save_memento()
                self.command_counter = 0
                command_file.truncate(0)
                command_file.seek(0)

    def save_memento(self):
        """
        Saving the whole inventory object in 'inventory.log' file
        :return:
        """
        memento = InventoryMemento(self.inventory_data)
        memento.save_memento()

    def get_state(self):
        """
        Load data from the 'inventory.log' file and set its state in the inventory object.
        :return:
        """
        memento = InventoryMemento(self.inventory_data)
        memento.get_memento()

    def replay_command(self, command_details):
        """
        Run the pending commands stored in the command.log file and populate the state of inventory object
        :param command_details:
        :return:
        """
        cmd = command_details[-1]
        book_name = command_details[0]
        book_price = command_details[1]
        book_id = command_details[2]
        book_price = command_details[3]
        # Commands are stored with an identifier, the identifier is fetched and the corresponding command is run
        if cmd == "ADD_BOOK":
            rebuild_book = Book(command_details[0], command_details[1], command_details[2], command_details[3])
            self.add_book(rebuild_book)
        if cmd == "SELL_BOOK":
            self.sell_book(book_id)
        if cmd == "CHANGE_PRICE":
            self.change_price_of_book(book_id, book_price)

    def run_pending_commands(self):
        """
        Read from command log file and return the commands to the replay command function.
        :return:
        """
        try:
            with open('command.log', 'r+') as file:
                for line in file.readlines():
                    line = line.strip('\n')
                    command_details = line.split(',')
                    self.replay_command(command_details)
                file.truncate(0)
                file.seek(0)
        except FileNotFoundError:
            print("Command file not yet populated!")
