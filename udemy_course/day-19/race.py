from turtle import Turtle, Screen
import random 

# Set up the screen
screen = Screen()
screen.setup(width=500, height=400)
bet = screen.textinput(title="Make your bet", prompt="Which color is going to win the race?")
print(bet)

# Set up color_list

color_list = ["red","orange","yellow","green","blue","purple"]
y_positions = [-100,-60,-20,20,60,100]
all_turtles = []

for turtle_index in range(0,6): 
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color_list[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-225,y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if bet:
    race_on = True
    
while race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            race_on = False
            winning_color = turtle.pencolor()
            if winning_color == bet:
                print("You win!")
            else:
                print("You've lost!")

        rand_dist = random.randint(0,10)
        turtle.forward(rand_dist)


screen.exitonclick()