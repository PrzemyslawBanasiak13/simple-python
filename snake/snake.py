from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
STEP_LEN = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segment_list = []
        for position in STARTING_POSITIONS:
            new_segment = Turtle(shape="square")
            new_segment.color("green")
            new_segment.penup()
            new_segment.goto(position)
            self.segment_list.append(new_segment)
            self.segment_list[0].color("yellow")
            self.segment_list[0].shape("square")
        self.head = self.segment_list[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle(shape="square")
            new_segment.color("green")
            new_segment.penup()
            new_segment.goto(position)
            self.segment_list.append(new_segment)
            self.segment_list[0].color("yellow")
            self.segment_list[0].shape("square")
        self.head = self.segment_list[0]

    def reset(self):
        for segment in self.segment_list:
            segment.goto(1000, 1000)
        self.segment_list.clear()
        self.create_snake()

    def grow(self):
        new_segment = Turtle(shape="square")
        x_cor = self.segment_list[len(self.segment_list) - 1].xcor()
        y_cor = self.segment_list[len(self.segment_list) - 1].xcor()
        new_segment.speed("fastest")
        new_segment.penup()
        new_segment.goto(x_cor, y_cor)
        self.segment_list.append(new_segment)
        new_segment.color("green")

    def move(self):

        for seg_num in range(len(self.segment_list) - 1, 0, -1):
            x_cor = self.segment_list[seg_num - 1].xcor()
            y_cor = self.segment_list[seg_num - 1].ycor()
            self.segment_list[seg_num].goto(x_cor, y_cor)
        self.segment_list[0].forward(STEP_LEN)

    def up(self):
        if not self.segment_list[0].heading() == DOWN:
            self.segment_list[0].setheading(UP)

    def down(self):
        if not self.segment_list[0].heading() == UP:
            self.segment_list[0].setheading(DOWN)

    def left(self):
        if not self.segment_list[0].heading() == RIGHT:
            self.segment_list[0].setheading(LEFT)

    def right(self):
        if not self.segment_list[0].heading() == LEFT:
            self.segment_list[0].setheading(RIGHT)
