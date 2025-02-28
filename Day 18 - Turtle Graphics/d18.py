import random
import colorgram
from turtle import Turtle, Screen



# Configuration
turtle = Turtle()
screen = Screen()
screen.colormode(255)
turtle.shape("turtle")
turtle.color('purple')
turtle.speed(0)
hirst_colors = colorgram.extract('hirst.jpg', 20)
hirst_colors = [color for color in hirst_colors if sum(tuple(color.rgb))/3 < 243]

def random_color():
    return tuple(random.choice(hirst_colors).rgb)

def draw_line():
    for _ in range(50):
        turtle.dot(10, random_color())
        turtle.penup()
        turtle.forward(20)
        turtle.pendown()
    turtle.dot(10)

def goes_up():
    turtle.setheading(90)
    turtle.penup()
    turtle.forward(20)
    turtle.pendown()
    print(turtle.position())
    if turtle.position()[0] < 0:
        turtle.setheading(0)
    else:
        turtle.setheading(180)

turtle.penup()
turtle.setposition(-500,-380)
turtle.pendown()

for _ in range(20):
    draw_line()
    goes_up()


screen.exitonclick()