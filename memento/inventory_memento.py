import json

class InventoryMemento:
    def __init__(self, inventory_data):
        self.inventory_data = inventory_data

    def save_memento(self):
        with open('inventory.log', 'w+') as file:
            file.write(json.dumps(self.inventory_data))
            file.close()

    def get_memento(self):
        try:
            with open('inventory.log', 'r') as inventory_file:
                inventory_content = inventory_file.read()
                self.inventory_data = json.loads(inventory_content)
        except json.JSONDecodeError:
            print("Memento file is empty! Proceeding")