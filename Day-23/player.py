from turtle import Turtle, Screen

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
SCREEN = Screen()


class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        SCREEN.tracer(0)
        self.setheading(90)
        self.goto(0, -280)
        SCREEN.update()
        
    def move(self):
        self.forward(10)