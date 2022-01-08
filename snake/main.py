import turtle
from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
game_is_on = True


def game_over():
    over_communicate = turtle.Turtle()
    over_communicate.hideturtle()
    over_communicate.penup()
    over_communicate.color("white")
    over_communicate.write(f"GAME OVER.", False, "center", ("system", 40, "normal"))
    time.sleep(1)
    over_communicate.clear()
    snake.reset()
    scoreboard.reset()


snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.grow()

    for segment in snake.segment_list[1:]:
        if snake.head.distance(segment) < 15:
            game_over()

    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        game_over()

screen.exitonclick()
