# random-walk

import random as r
from turtle import Turtle, Screen

t = Turtle()
t.pensize(5)

# t.colormode(255)


# def random_color():
#     re = r.randint(0, 255)
#     g = r.randint(0, 255)
#     b = r.randint(0, 255)
#     color = (re, g, b)
#     return color


# colours = random_color()

colours = ["red", "blue", "green", "yellow", "orange", "purple",
           "pink", "black", "grey", "brown", "cyan", "magenta"]

directions = [0, 90, 180, 270]

length = [30, 40, 50]

t.speed("fastest")


def line():
    t.color(r.choice(colours))
    t.forward(r.choice(length))
    t.right(r.choice(directions))


for i in range(100):
    line()


####################
screen = Screen()
screen.exitonclick()
