from math import pi, radians


class Circle:
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def get_area(self):
        return pi * self.radius ** 2

    def get_perimeter(self):
        return 2 * pi * self.radius


g = Circle(8)
