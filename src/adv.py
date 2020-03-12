# Standard library imports
import os
import sys
import textwrap
import time

# Local application imports
from room import Room
from player import Player
from consts import screen_width
from consts import sleep_value
from item import *

"""
BF comment: 
room is a dictonary with the values being objects that are instances of the room
class 
"""

# Declare all the items
items = {
    'hammer': Hammer(),
    'watch': Watch(),
    'box': Box(),
    'paper': Paper()
}

# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",
                     [items['hammer'], items['watch']]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
                     [items['box']]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
                     [items['paper']]),
}


"""
BF comment: 
A Room object has the attributes n_to, s_to, e_to, w_to that should be initially
set as None. Then here these attributes are set to point to a Room object, thus 
governing where a person can move to once he is in a certain room
"""
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

"""
BF comment:
Global variables
"""
end_game = False
user_input = ""


"""
BF comment:
Helper functions:
"""

"""
prints a line separator so that it is easy for the user to see
different time slices of the game
"""


def print_separator():
    print('~'*screen_width)


"""
returns a list which is one or two elements long. The first element is the action
word, the second element is a noun. The returned input will be verified
"""


def get_user_input():
    print('\nWhat do you want to do next?')
    user_options = "Your options are: n, s, e, w, q, i, 'get item', 'take item' 'drop item'"
    print(user_options)
    raw_input = input('> ')
    input_list = raw_input.split(' ')
    if len(input_list) > 2:
        print("You have entered more than 2 words, which is an incorrect option.")
        print('Beware of extra whitespace. Please try again...')
        time.sleep(sleep_value)
        return ["", None]
    if len(input_list) == 0:
        print("You have not made any choice.")
        print('Please try again...')
        time.sleep(sleep_value)
        return ["", None]
    if input_list[0] not in ['n', 's', 'e', 'w', 'q', 'i', 'get', 'take', 'drop']:
        print("You have not entered one of the correct options.")
        print('Beware of extra whitespace. Please try again...')
        time.sleep(sleep_value)
        return ["", None]
    if input_list[0] in ['n', 's', 'e', 'w', 'q', 'i'] and len(input_list) == 2:
        print("You have not entered one of the correct options.")
        print('Beware of extra whitespace. Please try again...')
        time.sleep(sleep_value)
        return ["", None]
    if input_list[0] in ['n', 's', 'e', 'w', 'q', 'i']:
        return [input_list[0], None]
    if input_list[0] in ['get', 'take', 'drop']:
        return [input_list[0], input_list[1]]


"""
checks if the item specified from taking or dropping is a valid item
"""


def validate_item_name(item_name, location):
    if item_name in items:
        return True
    else:
        print(
            f'The item {item_name} is not {location}')
        time.sleep(sleep_value)
        return False


# Make a new player object that is currently in the 'outside' room.
os.system('clear')
user_name = input("Hello user, please enter your name: ")
player = Player("user_name", room["outside"])
print(f"Ok {user_name}, let's play the game ...")
time.sleep(sleep_value)


# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
while not end_game:
    print_separator()
    player.current_room.describe_room()
    user_input = get_user_input()
    if user_input[0] == "q":
        end_game = True
    elif user_input[0] in ['n', 's', 'e', 'w']:
        player.move_to_room(user_input[0])
    elif user_input[0] in ['get', 'take']:
        if validate_item_name(user_input[1], 'in the room'):
            player.pick_up(items[user_input[1]])
    elif user_input[0] == "drop":
        # print(f'You want to drop the item: {user_input[1]}')
        if validate_item_name(user_input[1], 'in your inventory'):
            player.drop_down(items[user_input[1]])
    elif user_input[0] == 'i':
        player.display_inventory()

print('Thank you for playing')
