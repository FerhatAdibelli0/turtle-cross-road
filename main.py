import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
turtle_player = Player()
cars = CarManager()
scoreboard = Scoreboard()

screen.setup(width=600, height=600)
screen.tracer(0)

screen.listen()

screen.onkey(turtle_player.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_cars()
    cars.car_move()

    # Detect collision with car
    for car in cars.new_cars:
        if turtle_player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

    if turtle_player.is_finished():
        turtle_player.start_position()
        cars.speed_up()
        scoreboard.increase()
        scoreboard.update_scoreboard()

screen.exitonclick()
