import turtle 
import random

timmy = turtle.Turtle()
timmy.shape("classic")
timmy.speed("fastest")



color_list = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 179, 149), (14, 98, 71), (232, 176, 165),(101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102),(12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return (r,g,b)


turtle.colormode(255)

x_pos = -250 
y_pos = -250 

timmy.penup()
timmy.setx(x_pos)
timmy.sety(y_pos)
timmy.pendown()

def print_row():
    for i in range(10):
        color = random.choice(color_list)
        timmy.dot(20,color)
        timmy.penup()
        timmy.fd(50)

row_count = 0

while row_count < 10:
    print_row()
    row_count += 1
    y_pos += 50
    timmy.penup()
    timmy.setx(x_pos)
    timmy.sety(y_pos)
    timmy.pendown()

# timmy.penup()
# timmy.setx(-250)
# timmy.sety(-250)
# timmy.pendown()



# timmy.penup()
# timmy.setx(-250)
# timmy.sety(-200)
# timmy.pendown()

# for i in range(10):
#     color = random.choice(color_list)
#     timmy.dot(20,color)
#     timmy.penup()
#     timmy.fd(50)



screen = turtle.Screen()
screen.exitonclick() 





# 10 by 10
# 50 between dot
# 20 width 

