import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go, "Up")

game_is_on = True
while game_is_on:
    print(cars.car_speed)
    screen.update()
    cars.generate_cars_offscreen()
    cars.move()

    # check collision with a car
    for car in cars.cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False

    if player.ycor() > 280:
        scoreboard.level += 1
        scoreboard.update_scoreboard()
        player.go_to_start()
        cars.next_level_speedup()

screen.exitonclick()