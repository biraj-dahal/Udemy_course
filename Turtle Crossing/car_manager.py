from turtle import Turtle
import random

colors = ["black", "purple", "blue", "green", "yellow", "orange", "red", "pink"]


class Cars:
    MOVE_DISTANCE = 5

    def __init__(self):
        self.all_cars = []

    def create_cars(self):
        if random.randint(1, 6) == 3:
            new_car = Turtle('square')
            new_car.penup()
            new_car.turtlesize(stretch_wid=2, stretch_len=3)
            new_car.goto((600, random.randint(-350, 350)))
            new_car.color(random.choice(colors))
            new_car.setheading(180)
            self.all_cars.append(new_car)

    def move_allcars(self):
        for car in self.all_cars:
            car.forward(self.MOVE_DISTANCE)




    #
    # def random_location(self):
    #     ()



