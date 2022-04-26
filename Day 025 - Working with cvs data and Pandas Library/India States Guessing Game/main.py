from turtle import Turtle, Screen
import pandas

screen = Screen()
name_turtle = Turtle()
name_turtle.hideturtle()
name_turtle.up()
screen.setup(width=600, height=600)
screen.title("Name of States")
screen.bgpic('India.gif')

data = pandas.read_csv("states_data.csv")

states_dict = {}
for (state_name, x_cor, y_cor) in zip(data.Name.to_list(), data.x.to_list(), data.y.to_list()):
    states_dict[state_name] = (int(x_cor), int(y_cor))

while len(states_dict) > 0:
    guess = screen.textinput("Guess a State!!!", prompt="Input Here").upper()
    print(guess)
    if guess in states_dict:
        name_turtle.goto(states_dict[guess])
        name_turtle.write(guess)
        del states_dict[guess]

name_turtle.clear()
name_turtle.goto(0,0)
name_turtle.write("CONGRATULATIONS!!!!", font=30)
screen.exitonclick()
