from ursina import *
from score import *
from random import uniform


"""
This describes the point to be
"""


point_sound = Audio(sound_file_name="assets/shoot23.wav", autoplay=False, loop=False)


class Point(Button):
    def __init__(self, scale):
        super().__init__(
            model="circle",
            parent=camera.ui,
            scale=scale,
            color=color.white,
            position=(0, 0),
        )
        self.velocity = 0.04
        self.scaled = self.scale

    def on_click(self):

        setattr(Score, "score_number", getattr(Score, "score_number") + 1)
        self.position = (uniform(-0.86, 0.86), uniform(-0.47, 0.47))
        self.scale = self.scaled
        point_sound.play()

    def update(self):

        if self.scale > 0 and self.enabled:
            self.scale -= self.velocity * time.dt
        elif self.scale <= 0 and self.enabled:
            setattr(Missed, "missed_number", getattr(Missed, "missed_number") + 1)
            self.position = (uniform(-0.86, 0.86), uniform(-0.47, 0.47))
            self.scale = self.scaled

    def input(self, key):

        if key == "left mouse down" and not self.hovered:
            setattr(Missed, "missed_number", getattr(Missed, "missed_number") + 1)
