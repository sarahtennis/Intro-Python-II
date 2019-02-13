# information for visitable room
# items: list of items in room

class Room:
    def __init__(self, name, description, items = [], n_to = None, s_to = None, e_to = None, w_to = None):
        self.name = name
        self.description = description
        self.items = items
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to

    def getNeighbor(self, direction):
        if direction.lower() == "n":
            if self.n_to:
                return self.n_to
        elif direction.lower() == "e":
            if self.e_to:
                return self.e_to
        elif direction.lower() == "s":
            if self.s_to:
                return self.s_to
        elif direction.lower() == "w":
            if self.w_to:
                return self.w_to
        else: 
            return False