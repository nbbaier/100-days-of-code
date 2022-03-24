from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time 

# Set up the screen 

screen = Screen()
screen.setup(width=800,height=800)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0) 

## three square snake body 20x20 

scoreboard = Scoreboard()
snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.09)
    snake.move()
        
    # detect collision with food

    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()
        
    #  detect collision ith walls

    if snake.head.xcor() > 399 or snake.head.xcor() < -399 or snake.head.ycor() > 399 or snake.head.ycor() < -399:
        game_on = False
        scoreboard.game_over()
    
    for segment in snake.body[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            scoreboard.game_over()
        

screen.exitonclick()