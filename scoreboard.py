from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(x=0, y=265)
        self.hideturtle()
        self.score_update()
    def score_update(self):
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=("Arial", 24, "normal"))
    def increase(self):
        self.score+=1
        self.clear()
        self.score_update()


