
from turtle import Turtle
import random

y_cord_list = [-200, -180, -160, -140, -120, -100, -80, -60, -40, -20, 0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200]


class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.step = 0
        self.setheading(180)
        self.shape("square")
        self.color("blue")
        self.penup()
        self.goto(random.randint(-300, 300), random.choice(y_cord_list))

    def move(self):
        self.forward(self.step)

    def reset_pos(self):
        self.goto(340, random.choice(y_cord_list))
