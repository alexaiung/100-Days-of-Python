import random
from turtle import Turtle, Screen

def on_your_marks(colors, screen):
    turtles = generate_turtles(colors)
    send_turtles_initial_point(turtles)
    return start_race(turtles, screen)

def generate_turtles(colors):
    turtles = list()
    for i, color in enumerate(colors):
        turtles.append(Turtle('turtle'))
        turtles[i].color(color)
        turtles[i].penup()
        turtles[i].speed(0)
    return turtles

def send_turtles_initial_point(turtles):
    starting_point = 120
    for turtle in turtles:
        turtle.goto((-250, starting_point))
        starting_point -= 50

def walk_or_not(turtle):
    turtle.forward(random.randint(1, 10))

def start_race(turtles, screen):
    race_is_on = True
    while race_is_on:
        for i, turtle in enumerate(turtles):
            walk_or_not(turtle)
            if turtle.position()[0] >= (screen.screensize()[0]/2)+30:
                winner = turtle.color()[0].capitalize()
                print(f'{winner} is the winner!')
                return winner

def check_bet(bet, winner):
    if bet.capitalize() == winner:
        print('You won!')
    else:
        print('You lost!')

# Initial Configuration
screen = Screen()
screen.setup(500, 400)

# Starting the game
bet = screen.textinput(title='Make your bet!', prompt="Which turtle will win the race? Enter a color: ")

# Configuring the turtles
walk = False
colors = ['red', 'green', 'blue', 'purple', 'pink', 'yellow']
winner = on_your_marks(colors, screen)

check_bet(bet, winner)

screen.exitonclick()