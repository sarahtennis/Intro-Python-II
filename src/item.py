# base class for specialized item types
# Hint: name one word for parsing

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    # TODO: special action once an item is picked up into player inventory
    def on_take(self):
        pass
    
    # TODO: special action once an item is dropped into a room
    def on_drop(self):
        pass
