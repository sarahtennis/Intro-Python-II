# base class for specialized item types
# Hint: name one word for parsing

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description