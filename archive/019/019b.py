# turtle-race

from turtle import Turtle, Screen
import random

####################
# COLORS
colors = ["red", "green", "blue", "black", "gold"]
####################


####################
# SCREEN SETUP
s = Screen()
s.listen()
s.setup(width=600, height=600)
####################


####################
# INPUT
user_bet = s.textinput(title="Turtle Race", prompt="Enter your color: ")
print(user_bet)
####################


####################
# TURTLES
all_turtles = []
for i in range(0, 5):
    t = Turtle(shape="turtle")
    t.color(colors[i])
    t.penup()
    t.goto(x=-280, y=-100 + i * 50)
    all_turtles.append(t)
####################

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:

        if turtle.xcor() > 280:
            is_race_on = False

            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won! The {winning_color} turtle is the winner!")
                break
            else:
                print(f"You lost! The {winning_color} turtle is the winner!")
                break

        rand_dist = random.randint(0, 10)
        turtle.forward(rand_dist)


####################
s.exitonclick()
