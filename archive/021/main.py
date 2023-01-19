# snake-2

from turtle import Turtle, Screen
from random import randint
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


s = Screen()
s.bgcolor('black')
s.title('Snake')
s.setup(600, 600)
s.tracer(0)


my_snake = Snake()
my_food = Food()
my_scoreboard = Scoreboard()

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

    # Detect collision with food.
    if my_snake.head.distance(my_food) < 15:
        my_food.refresh()
        my_snake.extend()
        my_scoreboard.increase_score()

    # Detect collision with wall.
    if my_snake.head.xcor() > 280 or my_snake.head.xcor() < -280 or my_snake.head.ycor() > 280 or my_snake.head.ycor() < -280:
        game_is_on = False
        my_scoreboard.game_over()

    # Detect collision with tail.
    for segment in my_snake.segments:
        if segment == snake.head:
            pass
        elif my_snake.head.distance(segment) < 10:
            game_is_on = False
            my_scoreboard.game_over()


s.exitonclick()
