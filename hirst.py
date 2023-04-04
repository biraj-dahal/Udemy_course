import turtle
import colorgram
from turtle import *
import random
turtle.colormode(255)

colors = colorgram.extract("pallete.jpeg", 100)
colors_list = []
for i in colors:
    colors_list.append((i.rgb.r, i.rgb.g, i.rgb.b))

screen = Screen()
brz = turtle.Turtle()
brz.hideturtle()
brz.penup()
brz.speed("fastest")
brz.goto(-200, -200)
for dot_count in range(1, 101):
    brz.dot(20, random.choice(colors_list))
    brz.forward(50)
    if dot_count % 10 == 0:
        brz.left(90)
        brz.forward(50)
        brz.left(90)
        brz.forward(500)
        brz.left(180)


screen.exitonclick()
