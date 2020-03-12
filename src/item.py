import textwrap
from consts import screen_width


class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f'{self.name}'

    def on_take(self):
        print(f"You have picked up: {self.name}")
        item_info = f'Here is some information about this item: {self.description}'
        print(textwrap.fill(item_info, screen_width))

    def on_drop(self):
        print(f'You have dropped {self.name}')


class Hammer(Item):
    def __init__(self):
        super().__init__("hammer", "Use on nails")


class Watch(Item):
    def __init__(self):
        super().__init__("watch", "Tells the time")


class Paper(Item):
    def __init__(self):
        super().__init__("paper", "Has something written on it")


class Box(Item):
    def __init__(self):
        super().__init__("box", "Has something in it")
