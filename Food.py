from globals_ import WINDOW_SIZE
from Point import Point


class Food:
    def __init__(self, start=(0, 0), end=WINDOW_SIZE) -> None:
        self.pick_location(start, end)

    def pick_location(self, start=(0, 0), end=WINDOW_SIZE):
        self.position = Point.random(start, end)
