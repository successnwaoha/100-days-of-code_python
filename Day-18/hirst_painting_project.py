import turtle
import random

tim = turtle.Turtle()
turtle.colormode(255)
tim.speed(0)
tim.hideturtle()
color = [(194, 149, 131), (37, 17, 14), (140, 82, 58), (28, 106, 160), (237, 214, 85), (7, 22, 50), (220, 84, 64), (197, 137, 158), (120, 170, 195), (154, 62, 90), (158, 15, 33), (201, 81, 106), (161, 165, 30), (11, 53, 25), (126, 183, 156), (43, 127, 79), (78, 11, 20), (15, 94, 56), (137, 223, 208), (14, 177, 214), (10, 56, 140), (20, 201, 178), (156, 16, 11), (223, 172, 191), (235, 172, 160), (124, 220, 232)]

position = 50
tim.penup()
tim.setposition(-250, -220)
for _ in range(10):
    for _ in range(10):
        tim.dot(20, random.choice(color))
        tim.penup()
        tim.forward(50)
    tim.setposition(-250, position + (-220))
    position += 50
    



screen = turtle.Screen()
turtle.exitonclick()