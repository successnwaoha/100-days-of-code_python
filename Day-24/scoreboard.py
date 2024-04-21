from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 20, 'normal')

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High score: {self.high_score}", align=ALIGNMENT, move=False, font=FONT)
        
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg="GAME OVER", align=ALIGNMENT, move=False, font=FONT)
        
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()