# import colorgram
#
# colors = colorgram.extract('dots.jpg', 10)
#
# rgb_color = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color_tuple = (r, g, b)
#     rgb_color.append(color_tuple)
import turtle
from turtle import Turtle, Screen
import random
turtle.colormode(255)

lucy = Turtle()
lucy.speed("fastest")
lucy.penup()

color_list = [(26, 108, 164), (193, 38, 81), (237, 161, 50), (234, 215, 86), (227, 237, 229), (223, 137, 176),
              (143, 108, 57)]

for y in range(0, 500, 50):
    lucy.setpos(-200, -200+y)
    for x in range(0, 500, 50):
        lucy.down()
        lucy.dot(20, random.choice(color_list))
        lucy.up()
        lucy.forward(50)

screen = Screen()
screen.exitonclick()
