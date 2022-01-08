from turtle import Turtle
import random

cords_list = [-280, -260, -240, -220, -200, -180, -160, -140, -120, -100, -80, -60, -40,
              -20, 0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280]


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("purple")
        self.speed("fastest")
        r_x = random.choice(cords_list)
        r_y = random.choice(cords_list)
        self.goto(r_x, r_y)

    def refresh(self):
        r_x = random.choice(cords_list)
        r_y = random.choice(cords_list)
        self.goto(r_x, r_y)
