from classes.figure import Figure


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

        if self.__is_valid_sides(sides):
            self.__sides = list()
            for i_elem in range(self.sides_count):
                self.__sides.append(sides[0])
        else:
            self.__sides = list()
            for i_elem in range(self.sides_count):
                self.__sides.append(1)

    def __is_valid_sides(self, sides):
        if (isinstance(sides, (list, tuple, set, frozenset, dict)) and
                len(sides) == 1):
            return True
        else:
            return False

    def get_sides(self):
        return self.__sides

    def get_volume(self):
        return self.__sides[0] ** 3