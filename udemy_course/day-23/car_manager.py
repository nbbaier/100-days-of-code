from turtle import Turtle
import random 

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5



class CarManager():
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        new_car = Turtle("square")
        new_car.color(random.choice(COLORS))
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.penup()
        new_car.goto(310,random.randint(-250,250))
        self.all_cars.append(new_car)
    
    def move_cars(self):
        for car in self.all_cars:
            new_x = car.xcor() - self.car_speed
            car.goto(new_x,car.ycor())
        
    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT
 
# todo -  Hint: generate a new car only every 6th time the game loop runs. If you get stuck, check the video walkthrough in Step 4. 