
from turtle import Turtle

UP = 90
DOWN = 270


class Racket:

    def __init__(self):
        self.segment_list = []
        for element in range(0, 4):
            element = Turtle()
            element.shape("square")
            element.color()
            element.penup()
            element.speed("fastest")
            element.setheading(UP)
            self.segment_list.append(element)

    def set_left(self):
        cords = [(-490, -30), (-490, -10), (-490, 10), (-490, 30)]
        index = 0
        for element in self.segment_list:
            element.goto(cords[index])
            element.color("white")
            index += 1

    def set_right(self):
        cords = [(490, -30), (490, -10), (490, 10), (490, 30)]
        index = 0
        for element in self.segment_list:
            element.goto(cords[index])
            element.color("white")
            index += 1

    def go_up(self):
        for element in self.segment_list:
            element.forward(40)

    def go_down(self):
        for element in self.segment_list:
            element.back(40)
