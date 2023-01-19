# turtle-motions

from turtle import Turtle, Screen

t = Turtle()
t.shape("turtle")
t.color("green")
t.speed('fastest')
t.pensize(2)


def move_forward():
    t.forward(100)


def move_backward():
    t.forward(-100)


def turn_left():
    t.left(90)


def turn_right():
    t.right(90)


s = Screen()
s.listen()
s.onkey(key="Up", fun=move_forward)
s.onkey(move_backward, "Down")
s.onkey(turn_left, "Left")
s.onkey(turn_right, "Right")

s.exitonclick()
