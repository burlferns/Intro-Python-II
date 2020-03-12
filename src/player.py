# Write a class to hold player information, e.g. what room they are in
# currently.
import time
from consts import screen_width
from consts import sleep_value

"""
BF comment:
Attributes: name, current_room

Methods:
move_to_room(new_room)
"""


class Player:
    def __init__(self, name, current_room, items=[]):
        self.name = name
        self.current_room = current_room
        self.items = items

    def move_to_room(self, direction):
        room_door = direction+'_to'
        new_room = getattr(self.current_room, room_door)
        if new_room == None:
            print('You cannot go in that direction. Please try again...')
            time.sleep(sleep_value)
        else:
            self.current_room = new_room

    def pick_up(self, item):
        try:
            self.current_room.items.index(item)
        except ValueError:
            print(f'The item {item} is not in the room')
            time.sleep(sleep_value)
        else:
            self.current_room.items.remove(item)
            self.items.append(item)
            item.on_take()
            time.sleep(sleep_value)

    def drop_down(self, item):
        try:
            self.items.index(item)
        except ValueError:
            print(f'The item {item} is not in your inventory')
            time.sleep(sleep_value)
        else:
            self.items.remove(item)
            self.current_room.items.append(item)
            item.on_drop()
            time.sleep(sleep_value)

    def display_inventory(self):
        if len(self.items) == 0:
            print('You have no items in your inventory')
        else:
            inven_items = ""
            items_len = len(self.items)
            for i, n in enumerate(self.items):
                inven_items += f'{n}'
                if i < items_len-1:
                    inven_items += ", "
            print(
                f'There are the follwing items in your inventory: {inven_items}')
        time.sleep(sleep_value)
