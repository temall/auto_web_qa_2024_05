from src.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, side_a):
        if side_a <= 0:
            raise ValueError("This is not going to be a square")
        super().__init__(side_a, side_a)

    def get_area(self):
        return self.side_a * self.side_a

    def get_perimetr(self):
        return (self.side_a + self.side_a) * 2


s = Square(4)
