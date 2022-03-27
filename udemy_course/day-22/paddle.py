from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,starting_pos):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(starting_pos)    

    def move_up(self):
        new_y = self.ycor() + 20 
        self.goto(self.xcor(),new_y)
        
    def move_down(self):
        new_y = self.ycor() - 20 
        self.goto(self.xcor(),new_y)