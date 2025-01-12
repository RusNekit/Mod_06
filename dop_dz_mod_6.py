import math


class Figure:
    sides_count = 0

    def __init__(self, sides=None,  color=None, filled=False):
        self.__color = color if color else (0, 0, 0)
        self.filled = filled
        self.__sides = sides

    def get_color(self):
        return self.__color

    def set_color(self, r, g, b):
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            self.__color = (r, g, b)

    def __is_valid_color(self, r, g, b):
        return 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255

    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count:
            self.__sides = list(new_sides)

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)


class Cube(Figure):
    sides_count = 12

    def __init__(self, color=None, side=None, filled=False):
        super().__init__(sides=[side] * 12 if side else None, color=color, filled=filled)

    def get_volume(self):
        return self._Figure__sides[0]**3


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color=None):
        super().__init__(color)

    def get_square(self):
        a, b, c = self.__sides
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))

    def set_sides(self, a, b, c):
        self.__sides = (a, b, c)

    def get_sides(self):
        return self.__sides


class Circle(Figure):
    sides_count = 1

    def __init__(self, color=None, radius=0):
        super().__init__(color)
        self.__radius = radius

    def get_radius(self):
        return self.__radius

    def get_square(self):
        return self.__radius**2 * math.pi


# Код для проверки:

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)

cube1 = Cube((222, 35, 130), 6)



# Проверка на изменение цветов:

circle1.set_color(55, 66, 77) # Изменится

print(circle1.get_color())

cube1.set_color(300, 70, 15) # Не изменится

print(cube1.get_color())



# Проверка на изменение сторон:

cube1.set_sides(5, 3, 12, 4, 5) # Не изменится

print(cube1.get_sides())

circle1.set_sides(15) # Изменится

print(circle1.get_sides())



# Проверка периметра (круга), это и есть длина:

print(len(circle1))



# Проверка объёма (куба):

print(cube1.get_volume())

