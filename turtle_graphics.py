import turtle
from turtle import Turtle, Screen
import random


screen = Screen()
screen.screensize(canvwidth=300,canvheight=300)
screen.bgcolor("black")

brz = Turtle()
brz.speed('fastest')
brz.shape('turtle')

directions = [0, 90, 180, 270]
turtle.colormode(255)

degree = 0
for i in range(120):
    brz.setheading(degree)
    brz.pencolor((random.randint(0, 255)), (random.randint(0, 255)), (random.randint(0, 255)))
    brz.circle(100)
    degree += 3

screen.exitonclick()

"""
Random walk
for i in range(200):
    brz.forward(30)
    brz.setheading(random.choice(directions))
    brz.pencolor((random.randint(0, 255)), (random.randint(0, 255)), (random.randint(0, 255)))
"""

"""
Square
for i in range(4):
    brz.forward(100)
    brz.left(90)
    """
"""
Dashed Line
for i in range(15):
    brz.pendown()
    brz.forward(10)
    brz.penup()
    brz.forward(10)
"""