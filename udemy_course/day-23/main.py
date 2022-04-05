from re import I
import time
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_mgr = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move,"Up")

STARTING_SPAWN_RATE = 8
spawn_rate = STARTING_SPAWN_RATE

count = 0 

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_mgr.move_cars()
    
    ## spawn cars
    count += 1
    
    if count % spawn_rate == 0:
        car_mgr.create_car()
    
    ## check for colisions 
    for car in car_mgr.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()
            
    # detect the turtle getting across 
    if player.ycor() > FINISH_LINE_Y:
        player.level_up()
        scoreboard.point()
        scoreboard.update_score()
        car_mgr.increase_speed()
        # if spawn_rate > 6:
        #     spawn_rate -= 1            

screen.exitonclick()
