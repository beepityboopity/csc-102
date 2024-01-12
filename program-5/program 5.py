#####################
# Program 5
# Geometry go brrr
# ###################
# 10/13/2023
#####################

# shape class
class Shape:
    def __init__(self, width=1, height=1):  # default variables for width and height
        self.width = width
        self.height = height

    # getters and setters for width and height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value
        else:
            self._width = 1

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value > 0:
            self._height = value
        else:
            self._height = 1

    def __str__(self):  # __str__ function to print the shape
        x = ""
        for i in range(self.height):
            x += "* " * self.width
            x += "\n"
        return x


class Rectangle(Shape):  # rectangle class
    def __init__(self, width, height):
        super().__init__(width, height)


class Square(Shape):  # square class
    def __init__(self, width):
        super().__init__(width, width)


class Triangle(Shape): # triangle class
    def __init__(self, width):
        super().__init__(width, width)

    def __str__(self):  # __str__ function to print the triangle
        x = ""
        for i in range(self.width):
            x += "* " * (self.width - i)
            x += "\n"
        return x


class Parallelogram(Shape):  # Parallelogram class
    def __init__(self, width, height):
        super().__init__(width, height)

    def __str__(self):  # __str__ function to print the parallelogram
        x = ""
        for i in range(self.height):
            x += " " * (self.height - i)  # gives slanted shape
            x += "* " * self.width
            x += "\n"
        return x


# test everything

r1 = Rectangle(12, 4)
print(r1)
s1 = Square(6)
print(s1)
t1 = Triangle(7)
print(t1)
p1 = Parallelogram(10, 3)
print(p1)
r2 = Rectangle(0, 0)
print(r2)
p1.width = 2
p1.width = -1
p1.height = 2
print(p1)
