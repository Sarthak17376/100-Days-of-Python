from turtle import Turtle, Screen

james = Turtle()

for i in range(6):
    james.forward(10)
    james.penup()
    james.forward(10)
    james.pendown()

screen = Screen()
screen.exitonclick()
