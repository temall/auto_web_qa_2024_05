from math import pi, radians


class Circle:
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Radius can`t be less than 0")

        self.radius = radius

    @property
    def get_area(self):
        return pi * self.radius ** 2

    @property
    def get_perimeter(self):
        return 2 * pi * self.radius
