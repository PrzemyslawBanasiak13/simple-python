
from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()

        self.hideturtle()
        self.penup()
        self.score = 0
        self.goto(0, 260)
        self.color("white")
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", False, "center", ("system", 20, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()
