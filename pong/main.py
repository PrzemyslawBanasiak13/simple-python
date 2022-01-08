
from turtle import Screen, Turtle
import racket
import ball
import time
import random

import scoreboard

game_is_on = True

screen = Screen()
screen.setup(width=1024, height=576)
screen.bgcolor("black")
screen.tracer(0)


def draw_center_line():
    """draws line in center of screen from top to bottom"""
    lineman = Turtle()
    lineman.hideturtle()
    lineman.penup()
    lineman.color("white")
    lineman.shape("square")
    lineman.speed("fastest")
    lineman.goto(0, screen.window_height() / 2)
    lineman.setheading(270)
    lineman.pensize(3)
    lineman.forward(20)
    while lineman.ycor() > - screen.window_height() / 2:
        lineman.pendown()
        lineman.forward(20)
        lineman.penup()
        lineman.forward(20)


left_racket = racket.Racket()
left_racket.set_left()
screen.onkey(left_racket.go_up, "w")
screen.onkey(left_racket.go_down, "s")

right_racket = racket.Racket()
right_racket.set_right()
screen.onkey(right_racket.go_up, "Up")
screen.onkey(right_racket.go_down, "Down")

draw_center_line()

left_score = scoreboard.Scoreboard()
left_score.set_left()
right_score = scoreboard.Scoreboard()
right_score.set_right()

ball = ball.Ball()
ball.reset_pos()

screen.listen()

while game_is_on:
    screen.update()
    time.sleep(0.015)
    ball.move()

    if ball.ycor() >= (576 / 2) - 20 or ball.ycor() <= (-576 / 2) + 20:
        ball.setheading(- ball.heading())

    for element in left_racket.segment_list:
        if ball.distance(element) <= 15:
            ball.setheading(180 - ball.heading() + random.randint(-20, 20))

    for element in right_racket.segment_list:
        if ball.distance(element) <= 15:
            ball.setheading(180 - ball.heading() + random.randint(-20, 20))

    if ball.xcor() > 502:
        left_score.add_score()
        left_score.update_score()
        ball.reset_pos()
        screen.update()
        time.sleep(3)

    if ball.xcor() < -502:
        right_score.add_score()
        right_score.update_score()
        ball.reset_pos()
        screen.update()
        time.sleep(3)

screen.exitonclick()
