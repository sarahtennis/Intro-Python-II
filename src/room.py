from item import Item

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

    # returns neighboring room in argument direction, else False
    def get_neighbor(self, direction):
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

    # formats output to display all items currently in room
    def get_items(self):
        if len(self.items):
            output = []

            for item in self.items:
                output.append(item.name)
        
            return ', '.join(output)
        else:
            return 'Nothing'

    # if able, removes item from room and puts in user inventory --> returns true
    # item is string name from user input
    # NOTE: boolean return currently unused
    def room_to_inventory(self, item, player):
        if len(self.items):
            to_remove = list(filter(lambda x: x.name.lower() == item.lower(), self.items))

            if len(to_remove):
                to_remove = to_remove[0]
            else:
                print("\n\033[31mThat item is not in this room.\033[0m\n")
                return False

            # removes item from room --> adds item to player inventory --> runs item method on_take
            self.items.remove(to_remove)
            player.add_item(to_remove)
            to_remove.on_take()

            print(f"\n\033[32m{player.name} picks up {to_remove.name}\033[0m\n")
            return True
        else:
            print("\n\033[31mThere are no items in this room.\033[0m\n")
            return False
    
    def add_item(self, item):
        self.items.append(item)