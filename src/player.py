# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, location, inventory = []):
        self.name = name
        self.location = location
        self.inventory = inventory

    # adds item to user inventory
    def add_item(self, item):
        self.inventory.append(item)

    # returns formatted user inventory
    def get_inventory(self):
        if len(self.inventory):
            output = []

            for item in self.inventory:
                output.append(f"{item.name} - {item.description}")
        
            return '\n'.join(output)
        else:
            return 'Nothing'

    # if able, removes item from room and puts in user inventory --> returns true
    # item is string name from user input
    # NOTE: boolean return currently unused
    def inventory_to_room(self, item, room):
        if len(self.inventory):
            to_remove = list(filter(lambda x: x.name.lower() == item.lower(), self.inventory))

            if len(to_remove):
                to_remove = to_remove[0]
            else:
                print("\n\033[31m{self.name} is not carrying that item.\033[0m\n")
                return False

            # removes item from player inventory --> adds item to room --> runs item method on_drop
            self.inventory.remove(to_remove)
            room.add_item(to_remove)
            to_remove.on_drop()

            print(f"\n\033[32m{self.name} drops {to_remove.name}\033[0m\n")
            return True
        else:
            print("\n\033[31m{self.name} is not carrying that item.\033[0m\n")
            return False
