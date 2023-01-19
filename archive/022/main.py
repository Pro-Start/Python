from turtle import Turtle, Screen
from paddle import Paddle
import time
from scoreboard import Scoreboard
from separator import Separator
from ball import Ball

game_screen = Screen()
game_screen.bgcolor('black')
game_screen.title('Pong')
game_screen.setup(800, 600)
game_screen.listen()


p1 = Paddle((350, 0))
p2 = Paddle((-350, 0))

my_scoreboard = Scoreboard()
my_seperatator = Separator()
my_ball = Ball()

game_screen.onkey(p1.up, "w")
game_screen.onkey(p1.down, "s")
game_screen.onkey(p2.up, "Up")
game_screen.onkey(p2.down, "Down")


#       for no animation
game_is_on = True
# game_screen.tracer(0)
while game_is_on:
    # game_screen.update()
    time.sleep(0.01)
    my_ball.move()

    if my_ball.ycor() > 280 or my_ball.ycor() < -280:
        my_ball.bounce_y()

    if my_ball.distance(p1) < 50 and my_ball.xcor() > 320 or my_ball.distance(p2) < 50 and my_ball.xcor() < -320:
        my_ball.bounce_x()

    if my_ball.xcor() > 380:
        my_ball.reset_position()
        my_scoreboard.l_point()

    if my_ball.xcor() < -380:
        my_ball.reset_position()
        my_scoreboard.r_point()


game_screen.exitonclick()
