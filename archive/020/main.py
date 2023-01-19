# snake-1
from turtle import Turtle, Screen
from random import randint
import time
from snake import Snake


###################
# SCREEN
s = Screen()
s.bgcolor('black')
s.title('Snake')
s.setup(600, 600)
s.tracer(0)
###################

my_snake = Snake()

s.listen()
s.onkey(my_snake.up, "Up")
s.onkey(my_snake.down, "Down")
s.onkey(my_snake.left, "Left")
s.onkey(my_snake.right, "Right")


game_is_on = True
while game_is_on:
    s.update()
    time.sleep(0.1)
    my_snake.move()

    # if my_snake[0].xcor() > 300 or my_snake[0].xcor() < -300 or my_snake[0].ycor() > 300 or my_snake[0].ycor() < -300:
    #     game_is_on = False


s.exitonclick()
