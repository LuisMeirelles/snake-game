class Vector:
    def __init__(self, components: tuple[int, int]) -> None:
        self._x, self._y = components

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x: int):
        self._x = int(x)

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y: int):
        self._y = int(y)
