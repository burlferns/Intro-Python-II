# Implement a class to hold room information. This should have name and
# description attributes.
import textwrap
from consts import screen_width

"""
BF comment:
Attributes: name, description, n_to, s_to, e_to, w_to
Attribute default: n_to, s_to, e_to, w_to should be None

"""


class Room():
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def describe_room(self):
        print(f'Your location: {self.name}')
        print(f'{textwrap.fill(self.description,screen_width)}')

    def __str__(self):
        return f'This is the room: {self.name}'
