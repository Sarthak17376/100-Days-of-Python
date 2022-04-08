import turtle
from turtle import Turtle, Screen
import random

lucy = Turtle()
turtle.colormode(255)


def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_tuple = (r, g, b)
    return color_tuple


direction = [90, 180, 270]

lucy.width(10)
lucy.speed("fastest")
for i in range(100):
    lucy.color(random_colour())
    nsew = random.choice(direction)
    lucy.forward(30)
    lucy.setheading(nsew)

screen = Screen()
screen.exitonclick()
