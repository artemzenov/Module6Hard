class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        if self.__is_valid_color(color):
            self.__color = list(color)
        else:
            self.__color = (255, 255, 255)

        if self.__is_valid_sides(sides):
            self.__sides = list(sides)
        else:
            self.__sides = list()
            for i_elem in range(self.sides_count):
                self.__sides.append(1)

        if sum(self.__color) == 255 * 3:
            self.filled = False
        else:
            self.filled = True

    def get_color(self):
        return self.__color

    def get_sides(self):
        return self.__sides

    def __is_valid_color(self, color):
        if (isinstance(color, (list, tuple, set, frozenset, dict)) and
            len(color) == 3):
            for i_color in color:
                if (isinstance(i_color, int) and
                    0 <= i_color <= 255):
                    continue
                else:
                    return False
            else:
                return True
        else:
            return False

    def __is_valid_sides(self, sides):
        if (isinstance(sides, (list, tuple, set, frozenset, dict)) and
            len(sides) == self.sides_count):
            for i_side in sides:
                if isinstance(i_side, int) and i_side > 0:
                    continue
                else:
                    return False
            else:
                return True
        else:
            return False

    def set_color(self, *color):
        if self.__is_valid_color(color):
            self.__color = list(color)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(new_sides):
            self.__sides = list(new_sides)

    def __len__(self):
        return sum(self.__sides)