
from turtle import Turtle
SAVE_FILE = "score.txt"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()

        self.hideturtle()
        with open(SAVE_FILE, mode="r") as file:
            self.high_score = int(file.read())
            file.close()
        self.penup()
        self.score = 0
        self.goto(0, 270)
        self.color("white")
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}      High Score: {self.high_score}", False, "center", ("system", 20, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(SAVE_FILE, mode="w") as file:
                file.write(str(self.score))
        self.score = 0
        self.update_score()
