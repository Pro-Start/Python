# basics-of-turtle


from turtle import Turtle, Screen

t = Turtle()

t.shape("turtle")
t.color("red")
t.pensize(5)

t.penup()
t.pendown()


def line():
    t.forward(100)
    t.right(90)


for i in range(4):
    line()


####################
screen = Screen()
screen.exitonclick()
