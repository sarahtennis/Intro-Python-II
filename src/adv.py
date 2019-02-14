import sys
import os

from room import Room
from player import Player
from item import Item

# Declare all items

item = {
    'rock': Item('Rock', 'A small boulder or a large pebble'),
    'lemon': Item('Lemon', "A yellow citrus fruit"),
    'lint': Item('Lint', "From a pocket that hasn't been cleaned in a while")
}

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [item['rock'], item['lemon']]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player("Zino", room['outside'], [item['lint']])

# prints "Adventure Game" to terminal
with open(os.path.join(sys.path[0], 'logo.txt'), 'r') as logo:
    for line in logo:
        print(line, end='')

# start menu options
print('\n\n{:11s}{:10s}\n'.format('[S]tart', '[Q]uit'))

while True:
    start_input = input('>> ')
    start_input = start_input.lower().split()

    if len(start_input) == 1:
        start_input = start_input[0]
        if start_input == 's':
            name_input = input('\n>> Name the adventurer: ')
            player = Player(name_input, room['outside'], [item['lint']])
            break
        elif start_input == 'q' or start_input == 'exit':
            print("\n\033[35mThanks for playing!\033[0m\n")
            sys.exit()
        else:
            pass

while True:

    print(f"\033[34m\n-----{player.location.name}-----")
    print(f"{player.location.description}\033[0m\n")
    
    
    while True:
        
        # change phrasing to be nicer
        user_input = input('>> User input: ')
        user_input = user_input.lower().split()
        
        # one word input
        if len(user_input) == 1:
            user_input = user_input[0]
            # cardinal directions to move
            if user_input == 'n' or user_input == 's' or user_input == 'e' or user_input == 'w':
                neighbor = player.location.get_neighbor(user_input)

                if neighbor:
                    player.location = neighbor
                    break
                else:
                    print('\n\033[31mCan\'t go that way. Try another direction.\033[0m\n')
            # quits game
            elif user_input == 'q' or user_input == 'exit':
                print("\n\033[35mThanks for playing!\033[0m\n")
                sys.exit()
            # displays user inventory
            elif user_input == 'i' or user_input == "inventory":
                print(f"\n\033[36mInventory:\n{player.get_inventory()}\033[0m\n")
            # displays items in room
            elif user_input == 'search' or user_input == 'look':
                print(f"\n\033[36mYou can see: {player.location.get_items()}\033[0m\n")
            else:
                print("\n\033[31mNothing happens.\033[0m\n")
        # two word input
        elif len(user_input) == 2:
            # transfers item from room to user inventory
            if user_input[0] == 'grab' or user_input[0] == 'take':
                player.location.room_to_inventory(user_input[1], player)
            # transfers item from user inventory to room
            elif user_input[0] == 'drop' or user_input[0] == 'remove':
                player.inventory_to_room(user_input[1], player.location)
            else:
                print("\n\033[31mNothing happens.\033[0m\n")
        # empty or 2+ word input
        else:
            print("\n\033[31mNothing happens.\033[0m\n")
    
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
