
from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")

    def update_score(self):
        self.clear()
        self.write(f"{self.score}", False, "center", ("system", 20, "normal"))

    def add_score(self):
        self.score += 1

    def set_left(self):
        self.goto(-50, 258)
        self.update_score()

    def set_right(self):
        self.goto(50, 258)
        self.update_score()
