from classes.figure import Figure
import math


class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        perimeter = sum(self.get_sides()) / 2
        return math.sqrt(
                         perimeter *
                         (perimeter - self.get_sides()[0]) *
                         (perimeter - self.get_sides()[1]) *
                         (perimeter - self.get_sides()[2])
                        )