from idlelib.configdialog import is_int
from turtle import Turtle, Screen

class Snake():
    def __init__(self):
        self.snake_body = []
        size = 3
        position = 0
        for width in range(size):
            self.snake_body.append(Turtle())
            self.snake_body[-1].penup()
            self.snake_body[-1].shape('square')
            self.snake_body[-1].goto(position, 0)
            position -= 10

    def walk(self):
        for component in self.snake_body:
            component.forward(1)

    def go_up(self):
        self.snake_body[0].setheading(90)
        self.follow_up()

    def go_right(self):
        self.snake_body[0].setheading(0)

    def go_left(self):
        self.snake_body[0].setheading(180)

    def go_down(self):
        self.snake_body[0].setheading(270)

    def follow_up(self):
        for i, component in enumerate(self.snake_body):
            if i > 0:
                component.goto(self.snake_body[0].position()[0], self.snake_body[0].position()[i-1] - 10)
                component.setheading(90)



#snake = Snake()
screen = Screen()

turtles = []
position = 0
for i in range(10):
    turtles.append(Turtle("square"))
    turtles[-1].goto(position, 0)
    turtles[-1].penup()
    position -= 10


screen.listen()

def go_up():
    position_x_head = turtles[0].position()[0]
    turtles[0].setheading(90)
    for i, turtle in enumerate(turtles):
        while turtle.position()[0] < position_x_head:
            for t in turtles:
                t.forward(5)
        #turtle.setheading(90)

screen.onkey(go_up, "Up")
#screen.onkey(snake.go_right, "Right")
#screen.onkey(snake.go_down, "Down")
#screen.onkey(snake.go_left, "Left")

is_on = True
while is_on:
#    snake.walk()
    for component in turtles:
        component.forward(5)

screen.exitonclick()