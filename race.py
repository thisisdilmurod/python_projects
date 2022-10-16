import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bat = screen.textinput(title="Make your bat", prompt="Which turtle will win the race? Enter a color: ")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_positions = [-70, -40, -10, 20, 50, 80]
turtles = []


for turtle_index in range(0, 6):
    new_turtle = Turtle("turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(-230, y_positions[turtle_index])
    turtles.append(new_turtle)

if user_bat:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
        if turtle.xcor() > 230:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bat:
                screen.textinput(title="Results", prompt=f"You've won! The {user_bat} turtle is the winner!\nEnter your comments below: ")
            else:
                screen.textinput(title="Results", prompt=f"You've lost! The {winning_turtle} turtle is the winner!\nEnter your comments below: ")

screen.exitonclick()
