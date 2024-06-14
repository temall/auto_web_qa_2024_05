from math import sqrt


class Triangle:
    def __init__(self, side_a, side_b, side_c):
        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError("The triangle cannot be created with negative digits")
        if side_a == side_b and side_b == side_c:
            pass

        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    @property
    def get_area(self):
        s = (self.side_a + self.side_b + self.side_c) / 2
        return sqrt(s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c))

    @property
    def get_perimetr(self):
        return self.side_a + self.side_b + self.side_c
