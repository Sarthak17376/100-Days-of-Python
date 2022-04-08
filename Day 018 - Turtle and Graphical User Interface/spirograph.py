import turtle
from turtle import Turtle, Screen
import random

lucy = Turtle()
lucy.speed("fastest")

turtle.colormode(255)


def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_tuple = (r, g, b)
    return color_tuple


def draw_spirograph(size, radius):
    for i in range(int(360/size)):
        lucy.color(random_colour())
        lucy.circle(radius)
        lucy.setheading(lucy.heading() + size)


draw_spirograph(10, 100)
screen = Screen()
screen.exitonclick()
