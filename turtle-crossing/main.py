
from turtle import Screen, Turtle
from crazy_turtle import CrazyTurtle
from car import Car
import time
import scoreboard

# car_image_list = ["car1.png", "car2.png", "car3.png", "car4.png", "car5.png", "car6.png"]
car_list = []
time_interval = 0.01
lowest_step = 0.2
image = "turtle.gif"
game_is_on = True


def game_over():
    end_sign.write("GAME OVER.", False, "center", ("system", 50, "normal"))
    screen.update()


end_sign = Turtle()
end_sign.hideturtle()
end_sign.color("white")
end_sign.write("", False, "center", ("system", 50, "normal"))

screen = Screen()
screen.setup(600, 600)
screen.bgpic("road.png")
screen.addshape(image)
screen.tracer(0)

crazy_turtle = CrazyTurtle()
screen.onkey(crazy_turtle.move, "w")

scoreboard = scoreboard.Scoreboard()

screen.listen()

for num in range(0, 15):
    car = Car()
    car.step = lowest_step
    car_list.append(car)
    lowest_step += 0.1

while game_is_on:
    screen.update()
    time.sleep(time_interval)

    for car in car_list:
        if car.distance(crazy_turtle) < 20:
            game_over()
            game_is_on = False

    for car in car_list:
        car.move()
        if car.xcor() < -340:
            car.reset_pos()

    if crazy_turtle.ycor() >= 220:
        for car in car_list:
            car.step += 0.2
        scoreboard.increase_score()
        crazy_turtle.reset_pos()

screen.exitonclick()
