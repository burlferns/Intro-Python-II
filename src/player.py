# Write a class to hold player information, e.g. what room they are in
# currently.
import time
from consts import screen_width

"""
BF comment:
Attributes: name, current_room

Methods: 
move_to_room(new_room)
"""


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def move_to_room(self, direction):
        room_door = direction+'_to'
        new_room = getattr(self.current_room, room_door)
        if new_room == None:
            print('You cannot go in that direction. Please try again...')
            time.sleep(1)
        else:
            self.current_room = new_room
