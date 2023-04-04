from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'pink', 'brown']
        self.shape('turtle')
        self.penup()
        self.turtlesize(stretch_wid=0.7, stretch_len=0.7)
        self.color(random.choice(self.colors))
        self.speed('fastest')
        self.refresh_food()

    def refresh_food(self):
        self.goto(random.randint(-380, 380), random.randint(-380, 330))
