from turtle import Turtle

FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.color("red")
        self.write(f"GAME OVER",align="center",font=('Courier New', 22, 'bold'))

    def update_score(self):
        self.clear()
        self.goto(-280,270)
        self.write(f"Level: {self.score}",align="left",font=FONT)
     
    def point(self):
        self.score += 1