from src.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, side_a):
        if side_a <= 0:
            raise ValueError("The square cannot be created with negative digits")
        super().__init__(side_a, side_a)

