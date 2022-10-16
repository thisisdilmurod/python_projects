from turtle import Turtle, Screen
import random

tim = Turtle()

tim.pensize(5)
tim.speed("fastest")

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']


def draw(size_of_gap):
    for i in range(int(360/ size_of_gap)):
        tim.circle(100)
        tim.color(random.choice(colors))
        current_heading = tim.heading()
        tim.setheading(current_heading + size_of_gap)


draw(15)


screen = Screen()
screen.exitonclick()