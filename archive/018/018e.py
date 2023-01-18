# hirst-painting

import random as r
from turtle import Turtle, Screen
import colorgram as cg
import math


# # Extract 6 colors from an image.
# colours = cg.extract("../../../assets/hirst_painting.png", 6)
# rgb_colours = []
# for color in colours:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colours.append(new_color)

t = Turtle()
t.pensize(1)

colours = ["red", "blue", "green", "yellow", "orange", "purple",
           "pink", "black", "grey", "brown", "cyan", "magenta"]


t.speed("fastest")

####################
# CONFIG
total_dots = 49
dot_gap = 50
dot_size = 15
####################

actual_dot = math.ceil(math.sqrt(total_dots))
side_length = int(math.ceil(dot_gap * actual_dot))


def init_position():
    t.penup()
    t.right(135)
    t.forward(side_length/2)
    t.left(135)
    t.pendown()


def flip_sided():
    t.penup()
    t.left(90)
    t.forward(dot_gap)
    t.left(90)
    t.forward(side_length)
    t.pendown()
    t.right(180)


def draw_dot():
    t.color(r.choice(colours))
    t.dot(dot_size)


init_position()
for i in range(actual_dot):
    for i in range(actual_dot):
        draw_dot()
        t.penup()
        t.forward(dot_gap)
        t.pendown()

    flip_sided()


####################
screen = Screen()
screen.exitonclick()
