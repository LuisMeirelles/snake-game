from globals_ import WINDOW_SIZE
from Point import Point


class Food:
    def __init__(self) -> None:
        self.pick_location()

    def pick_location(self):
        self.position = Point.random(WINDOW_SIZE)
