
# ? Clases abstractas
# todo: Sirve como plantillas.
# todo: Se define con el módulo abc.

from abc import ABC, abstractmethod


class Figure(ABC):
    @abstractmethod
    def area(self):
        pass


class Square(Figure):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


square = Square(4)
print("Area of the square: ", square.area())
