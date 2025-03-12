from turtle import Turtle, Screen

from colorama.ansi import clear_screen

screen = Screen()
turtle = Turtle()

def move_forward():
    turtle.forward(10)

def move_backward():
    turtle.back(10)

def move_right():
    turtle.right(10)

def move_left():
    turtle.left(10)

def clear():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()

screen.listen()
screen.onkeypress(move_forward, 'w')
screen.onkeypress(move_backward, 's')
screen.onkeypress(move_left, 'a')
screen.onkeypress(move_right, 'd')
screen.onkey(clear, 'c')

screen.exitonclick()