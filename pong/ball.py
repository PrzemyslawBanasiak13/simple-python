from turtle import Turtle
import random

HEADING_LIST = [10, 20, 30, 40, 50, 60, 70, 110, 120, 130, 140, 150, 160, 170, 190,
                200, 210, 220, 230, 240, 250, 290, 300, 310, 320, 330, 340, 350]


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")

    def reset_pos(self):
        self.goto(0, 0)
        self.setheading(random.choice(HEADING_LIST))

    def move(self):
        self.forward(10)
