import random
from turtle import Turtle, Screen

is_race_on = True

screen = Screen()
screen.setup(width=500, height=400)
bet = screen.textinput(title="Make your bet!!", prompt="Which Turtle will win?(input color)")
colors = ["violet", "blue", "green", "yellow", "orange", "red"]

T1 = Turtle()
T2 = Turtle()
T3 = Turtle()
T4 = Turtle()
T5 = Turtle()
T6 = Turtle()

turtles = [T1, T2, T3, T4, T5, T6]
y = 150
c = 0
for i in turtles:
    i.shape("turtle")
    i.color(colors[c])
    i.penup()
    i.goto(-230, y)
    y -= 50
    c += 1

while is_race_on:
    for race_turtles in turtles:
        race_turtles.forward(random.randint(0, 10))
        if race_turtles.xcor() > 230:
            is_race_on = False
            winner = race_turtles.pencolor()
            if winner == bet:
                print(f"You Win!!! The Winner is {winner}")
            else:
                print(f"You lose!!! The Winner is {winner}")

screen.exitonclick()
