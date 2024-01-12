#############################
# ###################
# Program 3
# Randomly Generated Confetti
# 9/28/2023
#############################

import random
from random import choice
from math import sqrt
from tkinter import *


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    def dist(self, point2):
        return sqrt((self.x - point2.x)*(self.x - point2.x) + (self.y - point2.y)*(self.y - point2.y))

    def midpt(self, point2):
        return Point((self.x + point2.x)/2, (self.y + point2.y)/2)

    def __str__(self):
        return "({}, {})" .format(self.x, self.y)


class CoordinateSystem:
    def __init__(self, master=None):
        self.master = master
        self.canvas = Canvas(self.master)

    def plot(self, point, color):
        self.canvas.create_oval(point.x, point.y, point.x + 3, point.y + 3, fill=color, outline=color)

    def plotPoints(self, num=5000):
        colors = ["black", "cyan", "magenta", "red", "orange", "yellow", "green", "blue", "purple", "pink", "light green", "light blue"]

        for x in range(0, num):

            coord = Point(random.randint(0, 800), random.randint(0, 800))
            self.plot(coord, choice(colors))

        self.canvas.pack(fill=BOTH, expand=1)


window = Tk()
stuff = CoordinateSystem(window)
stuff.plotPoints()
window.geometry("800x800")
window.mainloop()
