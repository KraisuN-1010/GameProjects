from turtle import Turtle,Screen
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0

    def display_score(self):
        self.clear()
        self.penup()
        self.goto(0,250)
        self.pencolor("white")
        self.write(f"Score:{self.score}",align="center",font=("arial",24,"bold"))
        self.hideturtle()
        self.score+=1
    def end_game(self):
        self.goto(0,0)
        self.write("Game Over!!",align="center",font=("arial",24,"bold"))
        