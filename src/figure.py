from abc import ABC, abstractmethod


class Figure(ABC):

    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimetr(self):
        pass

    def add_area(self, other_figure):
        if not isinstance(other_figure, Figure):
            raise ValueError("Figure can`t be added because it was not given")
        return self.get_area() + other_figure.get_area()
