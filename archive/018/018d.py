# spirograph

import random as r
from turtle import Turtle, Screen

t = Turtle()
t.pensize(1)

colours = ["red", "blue", "green", "yellow", "orange", "purple",
           "pink", "black", "grey", "brown", "cyan", "magenta"]


t.speed("fastest")

circles = 20
circle_gap = int(360 / circles)


def draw_circle(circle_gap):
    t.color(r.choice(colours))
    t.circle(100)
    t.left(circle_gap)


for i in range(circles):
    draw_circle(circle_gap)


####################
screen = Screen()
screen.exitonclick()
