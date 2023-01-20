import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

my_player = Player()
my_car_manager = CarManager()
my_scoreboard = Scoreboard()

screen.onkey(my_player.go_up, key='Up')
screen.onkey(my_player.go_left, key='Left')
screen.onkey(my_player.go_right, key='Right')


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    my_car_manager.create_car()
    my_car_manager.move_cars()

    # Detect collision with car
    for car in my_car_manager.all_cars:
        if car.distance(my_player) < 20:
            game_is_on = False
            my_scoreboard.game_over()
        if my_player.is_at_finish_line():
            my_player.goto(0, -280)
            my_car_manager.car_speed += 10
            my_scoreboard.increase_score()


screen.exitonclick()
