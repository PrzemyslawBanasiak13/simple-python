
from turtle import Turtle


class CrazyTurtle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.setheading(90)
        self.penup()
        self.goto(0, - 270)

    def reset_pos(self):
        self.goto(0, - 270)

    def move(self):
        self.forward(20)
