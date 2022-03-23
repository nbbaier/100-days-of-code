from turtle import Turtle, Screen

tim = Turtle()
tim.speed("fastest")

screen = Screen()
increment = 10

def move_forward():
    tim.fd(increment)

def move_back():
    tim.bk(increment)
    
def rotate_right():
    new_heading = tim.heading()-10
    tim.setheading(new_heading)


def rotate_left():
    new_heading = tim.heading()+10
    tim.setheading(new_heading)

def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(move_forward, "Up")
screen.onkey(move_back, "Down")
screen.onkey(rotate_left, "Left")
screen.onkey(rotate_right, "Right")
screen.onkey(clear_screen, "space")
screen.exitonclick()