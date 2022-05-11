from ursina import *


class MenuButton(Button):
    def __init__(self, text="", **kwargs):
        super().__init__(text, scale=(0.25, 0.075), highlight_color=color.red, **kwargs)

        for key, value in kwargs.items():
            setattr(self, key, value)
