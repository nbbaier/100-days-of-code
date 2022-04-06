from hashlib import new
from turtle import Turtle



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("scores.txt",'r') as file:
             self.high_score = int(file.read())
        self.color("white") 
        self.penup()
        self.goto(0,370)
        self.ht()
        self.update_score()

    def update_score(self):
        self.clear()        
        self.write(f"Score: {self.score} High Score: {self.high_score}",align="center",font=('Courier New', 18, 'normal'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("scores.txt",'w') as file:
                file.write(str(self.score)) 
        self.score = 0
        self.update_score()
        
    # def game_over(self):
    #     self.goto(0,0)
    #     self.color("red")
    #     self.write(f"GAME OVER",align="center",font=('Courier New', 20, 'bold'))
 
    def increase_score(self):
        self.score += 1
        self.update_score()