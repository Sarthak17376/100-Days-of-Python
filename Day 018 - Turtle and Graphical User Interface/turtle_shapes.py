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


lucy.speed(7)


for sides in range(3, 10):
    side_angle = 180 - (180 * (sides - 2) / sides)
    lucy.color(random_colour())
    for i in range(sides):
        lucy.forward(100)
        lucy.right(side_angle)

screen = Screen()
screen.exitonclick()
