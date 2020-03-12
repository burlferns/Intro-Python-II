# Implement a class to hold room information. This should have name and
# description attributes.
import textwrap
import time
from consts import screen_width
from consts import sleep_value


"""
BF comment:
Attributes: name, description, n_to, s_to, e_to, w_to
Attribute default: n_to, s_to, e_to, w_to should be None

"""


class Room():
    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = items

    def describe_room(self):
        print(f'Your location: {self.name}')
        print(f'{textwrap.fill(self.description,screen_width)}')
        if len(self.items) == 0:
            print('There are no items in this room')
        else:
            room_items = ""
            items_len = len(self.items)
            for i, n in enumerate(self.items):
                room_items += f'{n}'
                if i < items_len-1:
                    room_items += ", "
            print(f'There are the follwing items here: {room_items}')
        # time.sleep(sleep_value)

    def __str__(self):
        return f'This is the room: {self.name}'
