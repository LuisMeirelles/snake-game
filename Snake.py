from pygame import Color
from Food import Food
from Point import Point
from Vector import Vector


class Snake:
    def __init__(self, coordinates: Point, color: Color) -> None:
        self.position = coordinates
        self.velocity = Vector((1, 0))
        self.color = color
        self.total = 0
        self.tail = []

    def update(self):
        current_position = self.position.copy()

        if self.total == len(self.tail):
            for i in range(len(self.tail) - 1):
                self.tail[i] = self.tail[i+1]

            if len(self.tail):
                self.tail[-1] = current_position
        else:
            self.tail.append(current_position)

        self.position += self.velocity

    def move_up(self):
        self.velocity = Vector((0, -1))

    def move_down(self):
        self.velocity = Vector((0, 1))

    def move_left(self):
        self.velocity = Vector((-1, 0))

    def move_right(self):
        self.velocity = Vector((1, 0))

    def eat(self, food: Food):
        food.pick_location()

        self.total += 1
