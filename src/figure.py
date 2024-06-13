from abc import ABC, abstractmethod


class Figure(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimetr(self):
        pass

    def add_area(self, other_figure):
        if not isinstance(other_figure, Figure):
            raise ValueError("Can`t be added")
        return self.get_area() + other_figure.get_area()
