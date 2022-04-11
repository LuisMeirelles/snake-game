from __future__ import annotations
from globals_ import PIXEL_SIZE
import random


class Point:
    def __init__(self, coordinates: tuple[int, int]) -> None:
        self.x = coordinates[0] // PIXEL_SIZE * PIXEL_SIZE
        self.y = coordinates[1] // PIXEL_SIZE * PIXEL_SIZE

    @staticmethod
    def random(*coords) -> Point:
        if len(coords) == 2:
            min_x, min_y = coords[0]
            max_x, max_y = coords[1]
        else:
            min_x = min_y = 0

            max_x = coords[0][0] - PIXEL_SIZE
            max_y = coords[0][1] - PIXEL_SIZE

        random_x = random.randint(min_x, max_x)
        random_y = random.randint(min_y, max_y)

        point = Point((random_x, random_y))
        return point

    def copy(self):
        return Point((self.x, self.y))

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y

        return Point((x, y))

    def __iadd__(self, other):
        self.x += other.x * PIXEL_SIZE
        self.y += other.y * PIXEL_SIZE

        return self

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self) -> str:
        return f'({self.x}, {self.y})'
