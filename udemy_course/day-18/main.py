import turtle 
import random

timmy = turtle.Turtle()
timmy.shape("classic")
timmy.speed("fastest")

turtle.colormode(255)

def triangle():
    for i in range(3):
        timmy.forward(75)
        timmy.right(120)
def square():
    for i in range(4):
        timmy.forward(75)
        timmy.right(90)
def pentagon():
    for i in range(5):
        timmy.forward(75)
        timmy.right(72)
def hexagon():
    for i in range(6):
        timmy.forward(75)
        timmy.right(60)        
def heptagon():
    for i in range(7):
        timmy.forward(75)
        timmy.right(51.429)
def octagon():
    for i in range(8):
        timmy.forward(75)
        timmy.right(45)      
def nonagon():
    for i in range(9):
        timmy.forward(75)
        timmy.right(40)
def decagon():
    for i in range(10):
        timmy.forward(75)
        timmy.right(36)


angles = [0,90,180,270]

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r,g,b)

def random_walk():
    color = random_color()
    timmy.pencolor(color)
    timmy.forward(25)
    timmy.right(random.choice(angles))

# timmy.width(8)
# for i in range(200):
#     random_walk()

angle = 30
repeat = int(360/angle)
size = [40,60,80]

for i in range(repeat):
    color = random_color()
    timmy.pencolor(color)
    turtle.circle(random.choice(size))
    turtle.right(angle)

screen = turtle.Screen()

screen.exitonclick() 


