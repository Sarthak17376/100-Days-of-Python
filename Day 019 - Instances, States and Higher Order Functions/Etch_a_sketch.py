from turtle import Turtle, Screen
lucy = Turtle()


def move_forward():
    lucy.forward(10)


def move_backward():
    lucy.backward(10)


def move_counter_clock():
    lucy.left(10)


def move_clock():
    lucy.right(10)


def clear():
    lucy.clear()
    lucy.penup()
    lucy.home()
    lucy.down()


screen = Screen()
screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(move_clock, "d")
screen.onkey(move_counter_clock, "a")
screen.onkey(clear, "c")
screen.exitonclick()
