from turtle import Turtle, Screen
from random import choice
tim = Turtle()

tim.shape("turtle")

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

def draw_shapes(number_of_sides):
    angle = 360 / number_of_sides
    for _ in range(number_of_sides):
        tim.forward(100)
        tim.left(angle)

for shape_side_n in range(3, 11):
    tim.color(choice(colors))
    draw_shapes(shape_side_n)




screen = Screen()
screen.exitonclick()