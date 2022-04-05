from turtle  import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time 

# Set up the screen 

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle_r = Paddle((350,0))
paddle_l = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle_r.move_up,"Up")
screen.onkey(paddle_r.move_down,"Down")
screen.onkey(paddle_l.move_up,"w")
screen.onkey(paddle_l.move_up,"W")
screen.onkey(paddle_l.move_down,"s")
screen.onkey(paddle_l.move_down,"S")


game_on = True 
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    # Upper/lower bound collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Paddle collision 
    if ball.xcor() > 340 and ball.distance(paddle_r) < 55 or ball.xcor() < -340 and ball.distance(paddle_l) < 55:
        ball.bounce_x()
        
    # Right paddle miss
    if ball.xcor() > 380:
        scoreboard.l_point()
        scoreboard.update_score()
        ball.refresh()
    
    # Leff paddle miss 
    if ball.xcor() < -380:
        scoreboard.r_point()
        scoreboard.update_score()
        ball.refresh()

screen.exitonclick()
