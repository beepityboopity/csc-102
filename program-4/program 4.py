#####################
# ###################
# Program 4
# Triangles go brrrr
# 10/6/2023
#####################

# import libraries
import random
from math import sqrt
from tkinter import *

# point class, same as program 3
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

# chaos game class
class ChaosGame:

    # triangle vertices
    v1 = Point(3, 512)
    v2 = Point(592, 512)
    v3 = Point(300, 3)

    def __init__(self, master=None):
        # initialize canvas
        self.master = master
        self.canvas = Canvas(self.master)

    def plot_points(self, num=50000):
        # plot vertices
        self.canvas.create_oval(ChaosGame.v1.x, ChaosGame.v1.y, ChaosGame.v1.x + 5, ChaosGame.v1.y + 5, fill="red",
                                outline="red")
        self.canvas.create_oval(ChaosGame.v2.x, ChaosGame.v2.y, ChaosGame.v2.x + 5, ChaosGame.v2.y + 5, fill="red",
                                outline="red")
        self.canvas.create_oval(ChaosGame.v3.x, ChaosGame.v3.y, ChaosGame.v3.x + 5, ChaosGame.v3.y + 5, fill="red",
                                outline="red")

        # select random vertices and plot the midpoints
        p1, p2 = random.sample([ChaosGame.v1, ChaosGame.v2, ChaosGame. v3], 2)
        m = Point.midpt(p1, p2)
        self.canvas.create_oval(m.x, m.y, m.x + 2, m.y + 2, fill="black", outline="black")

        # plot the rest of the midpoints
        for x in range(0, num):
            v = random.choice([ChaosGame.v1, ChaosGame.v2, ChaosGame. v3])
            mv = Point.midpt(v, m)
            self.canvas.create_oval(mv.x, mv.y, mv.x + 2, mv.y + 2, fill="black", outline="black")
            m = mv
        # pack the canvas
        self.canvas.pack(fill=BOTH, expand=1)


window = Tk()  # make window
window.title("The Chaos Game")  # set title
stuff = ChaosGame(window)  # make the canvas
window.geometry("600x520")  # set geometry
stuff.plot_points()  # make the triangles
window.mainloop()
