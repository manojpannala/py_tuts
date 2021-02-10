# install pip package turtle

import turtle

man_turtle = turtle.Turtle()

def square():
    man_turtle.forward(100)
    man_turtle.right(90)
    man_turtle.forward(100)
    man_turtle.right(90)
    man_turtle.forward(100)
    man_turtle.right(90)
    man_turtle.forward(100)

def square2():
    man_turtle.forward(200)
    man_turtle.right(90)
    man_turtle.forward(200)
    man_turtle.right(90)
    man_turtle.forward(200)
    man_turtle.right(90)
    man_turtle.forward(200)

for count in range(8):
    square()