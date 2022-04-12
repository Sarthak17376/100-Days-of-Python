from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.up()
        self.score = 0
        self.create_scoreboard()

    def create_scoreboard(self):
        self.up()
        self.goto(0, 270)
        self.down()
        self.write(f"Score: {self.score}", align="center", font=12)
        self.up()

    def increase_score(self):
        self.clear()
        self.down()
        self.score += 1
        self.write(f"Score: {self.score}", align="center", font=12)
        self.up()
