from turtle import Turtle, Screen

tim = Turtle()
tim.shape("arrow")
tim.color("red")

# for i in range(4):
    # tim.forward(100)
    # tim.right(90)

# for i in range(10):
    # tim.forward(5)
    # tim.penup()
    # tim.forward(5)
    # tim.pendown()


def draw(sides):
    for i in range(sides):
        angle = 360/sides
        tim.forward(100)
        tim.right(angle)


for shape_side_n in range(3, 11):
    draw(shape_side_n)


screen = Screen()
screen.exitonclick()

# from turtle import Turtle -- import a certain class from the module
# import turtle as t -- rename and import the module
# import turtle -- import the whole module
# from turtle import * -- import every class from the module