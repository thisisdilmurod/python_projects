import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.pensize(5)
tim.speed("fastest")


def colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    color = (r, g, b)
    return color


directions = [0, 90, 180, 270]

while True:
    tim.color(colors())
    tim.forward(10)
    tim.setheading(random.choice(directions))
    tim.color(colors())

screen = Screen()
screen.exitonclick()
