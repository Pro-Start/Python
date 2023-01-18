# shapes

from turtle import Turtle, Screen

t = Turtle()

t.shape("turtle")
t.pensize(5)


colours = ["red", "blue", "green", "yellow", "orange", "purple",
           "pink", "black", "grey", "brown", "white", "cyan", "magenta"]


def line():
    t.forward(100)


def turn(this_angle):
    t.right(this_angle)


def angle(side):
    a = 180 - ((side - 2) * 180)/side
    return a


def shape(sides, color):
    t.color(color)
    a = int(angle(sides))
    for i in range(sides):
        line()
        turn(a)


for i in range(3, 10):
    shape(i, colours[i])


####################
screen = Screen()
# screen.exitonclick()
