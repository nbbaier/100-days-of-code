from hashlib import new
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0 
        self.color("white") 
        self.penup()
        self.goto(0,370)
        self.write(f"Score: {self.score}",align="center",font=('Courier New', 20, 'normal'))
        self.ht()

    def update_score(self):
        self.write(f"Score: {self.score}",align="center",font=('Courier New', 18, 'normal'))

    def game_over(self):
        self.goto(0,0)
        self.color("red")
        self.write(f"GAME OVER",align="center",font=('Courier New', 20, 'bold'))
 
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()