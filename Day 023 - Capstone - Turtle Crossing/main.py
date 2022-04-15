import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
scoreboard = Scoreboard()
screen.listen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()

game_is_on = True
while game_is_on:
    chance = random.randint(1, 6)
    if chance == 1:
        car.make_car()
    time.sleep(0.1)
    screen.update()
    car.move_car()
    screen.onkey(player.turtle_move, "w")
    for hit_turtle in car.cars_list:
        if (-10 < hit_turtle.xcor() < 25) and (-25 < hit_turtle.ycor() - player.ycor() < 25):
            game_is_on = False
    if player.ycor() == 280:
        scoreboard.increase_level()
        player.goto(0, -280)
        car.car_speed += 2

screen.exitonclick()
